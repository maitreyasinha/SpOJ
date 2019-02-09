num_input = int(input())
output_str = ""


def tetrahedron_volume(u, v, w, W, V, U):
    u_ = v**2 + w**2 - U**2
    v_ = w**2 + u**2 - V**2
    w_ = u**2 + v**2 - W**2
    return ((4 * (u*v*w)**2 - (u*u_)**2 - (v*v_)**2 - (w*w_)**2 + u_*v_*w_)**0.5) / 12


for tst_case in range(num_input):
    # [u, v, w, W, V, U]
    len_side  = [int(side) for side in input().split(" ")]
    output_str = output_str + "{0:.4f}".format(tetrahedron_volume(*len_side)) + "\n"

print(output_str)