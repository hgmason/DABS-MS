import torch

def loss_func(lrnr, small_combo_A, trans_pred, def_field): #all loss_funcs must have these inputs
    dy = torch.abs(def_field[:, :, 1:, :, :] - def_field[:, :, :-1, :, :])
    dx = torch.abs(def_field[:, :, :, 1:, :] - def_field[:, :, :, :-1, :])
    dz = torch.abs(def_field[:, :, :, :, 1:] - def_field[:, :, :, :, :-1])

    dy = dy * dy
    dx = dx * dx
    dz = dz * dz

    d = torch.mean(dx) + torch.mean(dy) + torch.mean(dz)
    grad = d / 3.0

    return grad