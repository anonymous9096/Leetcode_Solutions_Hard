def MOTSA(nums1, nums2):
    dum1, dum2 = nums1, nums2
    added2 = sorted(dum1 + dum2)
    # print(added2)
    if len(added2) % 2 == 0:
        x = float((added2[(len(added2)//2)-1] + added2[(len(added2)//2)]) / 2)
        return print(x)
    else:
        return print(added2[(len(added2))//2])


if __name__=="__main__":
    nums1 = list(int(input()))
    nums2 = list(int(input()))
    MOTSA(nums1, nums2)