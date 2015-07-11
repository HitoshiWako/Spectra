import numpy as np
from scipy.stats import cauchy
from scipy.optimize import curve_fit

def peak(x):
#�@���X�g����s�[�N�ƃ{�g���̈ʒu������
#�@���̈ʒu�Ɨ����̋�؂�i�s�[�N�ł���΃{�g���C�{�g���ł���΃s�[�N�j��
#�@�Ԃ��B�i�[�ł���΁C���X�g�̗��[���g���j

    c = np.sign(np.diff(x))
    c1 = np.append(0,c)
    c2 = np.append(c,0)
    p = np.where((c1 > 0) & (c2 < 0))[0].tolist()
    v = np.where((c1 < 0) & (c2 > 0))[0].tolist()

    bp = p
    bv = v
    
    if p[0] < v[0]:
        bv = [0] + bv
    else:
        bp = [0] + bp

    if p[-1] > v[-1]:
        bv = bv + [len(x)-1]
    else:
        bp = bp + [len(x)-1]

    pl = [(p[i],bv[i],bv[i+1]) for i in range(len(p))]
    vl = [(v[i],bp[i],bp[i+1]) for i in range(len(v))]
    
    return pl,vl

def lorentz(x, loc = 0, scale = 1, mag = 1):
#�@���[�����c�Ȑ��i�R�[�V�[���z�j�̐ݒ�    
    return cauchy.pdf(x, loc = loc, scale = scale)*mag

def lorentz_fit(x, y, loc, scale, mag):
#�@���[�����c�Ȑ��ł̃t�B�b�e�B���O
    return curve_fit(lorentz, x, y, p0 = [loc, scale, mag])

