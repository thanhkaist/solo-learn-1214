# Copyright 2021 solo-learn development team.

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import torch
import torch.nn.functional as F
from solo.utils.misc import gather, get_rank
import ipdb

### Our Loss defined here
def ours_loss_func(z1: torch.Tensor, z2: torch.Tensor, indexes: torch.Tensor, tau_decor: float = 0.1) -> torch.Tensor:
    """Computes Ours's loss given batch of projected features z
    from different views, a positive boolean mask of all positives and
    a negative boolean mask of all negatives.
    Args:
        z (torch.Tensor): (N*views) x D Tensor containing projected features from the views.
        indexes (torch.Tensor): unique identifiers for each crop (unsupervised)
            or targets of each crop (supervised).
    Return:
        torch.Tensor: Ours loss.
    """

    _, D = z1.size()
    bn = torch.nn.BatchNorm1d(D, affine=False).to(z1.device)
    z1 = bn(z1).T
    z2 = bn(z2).T

    z = torch.cat((z1, z2), dim=0)

    z = F.normalize(z, dim=-1)
    gathered_z = gather(z)

    ipdb.set_trace()

    sim = torch.exp(torch.einsum("if, jf -> ij", z, gathered_z) / tau_decor)

    gathered_indexes = gather(indexes)

    indexes = indexes.unsqueeze(0)
    gathered_indexes = gathered_indexes.unsqueeze(0)
    # positives
    pos_mask = indexes.t() == gathered_indexes
    pos_mask[:, z.size(0) * get_rank() :].fill_diagonal_(0)
    # negatives
    neg_mask = indexes.t() != gathered_indexes

    pos = torch.sum(sim * pos_mask, 1)
    neg = torch.sum(sim * neg_mask, 1)
    loss = -(torch.mean(torch.log(pos / (pos + neg))))
    return loss

### End of our loss
