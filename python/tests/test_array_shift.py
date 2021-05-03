from challenges.array_shift import __version__

from challenges.array_shift.array_shift import insertShiftArray


def test_version():
    assert __version__ == '0.1.0'


def test_array_shift_evenlength():

    #arrange
    expected=[2,4,5,6,8]
    actual=insertShiftArray([2,4,6,8], 5)
    assert expected==actual





def test_array_shift_oddlength():
    expected2=[4,8,15,16,23,42]
    actual2=insertShiftArray([4,8,15,23,42], 16	)
    assert expected2==actual2




def test_array_shift_faildtest():

    expected3='plz enter valid inputs'
    actual3=insertShiftArray([], 16	)
    actual4=insertShiftArray([4,8,15,23,42], 'val')
    assert expected3==actual3
    assert expected3==actual4












