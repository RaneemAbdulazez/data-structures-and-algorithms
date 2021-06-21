a

#W�`�  �                   @   sV   d dl Zd dlm  mZ d dlmZ d dlm	Z	 dd� Z
dd� Zdd	� Zd
d� Z
dS )�    N)�__version__)�insertShiftArrayc                  C   s|   d} t | k}|spt�d|fdt | f�dt�� v s:t�t �rDt�t �ndt�| �d� }dd|i }tt�|���d  }} d S )Nz0.1.0��==)z%(py0)s == %(py3)sr   )�py0�py3zassert %(py5)s�py5)	r   �
@pytest_ar�_call_reprcompare�@py_builtins�locals�_should_repr_global_name�	_saferepr�AssertionError�_format_explanation)�@py_assert2�@py_assert1�@py_format4�@py_format6� r   �\/home/raneem/codefellows/401/data-structures-and-algorithms/python/tests/test_array_shift.py�test_version   s    r   c                  C   s�   g d�} t g d�d�}| |k}|s�t�d|fd| |f�dt�� v sLt�| �rVt�| �nddt�� v snt�|�rxt�|�ndd� }d	d
|i }tt�|���d }d S )N)�   �   �   �   �   )r   r   r   r   r   r   �z%(py0)s == %(py2)s�expected�actual�r   �py2�assert %(py4)s�py4�	r   r	   r
   r   r   r
   r   r   r   )r   r   r   �@py_format3�@py_format5r   r   r   �test_array_shift_evenlength
   s    r'   c                  C   s�   g d�} t g d�d�}| |k}|s�t�d|fd| |f�dt�� v sLt�| �rVt�| �nddt�� v snt�|�rxt�|�ndd� }d	d
|i }tt�|���d }d S )N)r   r   �   �   �   �*   �r   r   r(   r*   r+   r)   r   r   �	expected2�actual2r    r"   r#   r$   )r-   r.   r   r%   r&   r   r   r   �test_array_shift_oddlength   s    r/   c                  C   s:  d} t g d�}t g d�d�}| |k}|s�t�d|fd| |f�dt�� v sRt�| �r\t�| �nddt�� v stt�|�r~t�|�ndd	� }d
d|i }tt�|���d }| |k}|�s2t�d|fd| |f�dt�� v s�t�| �r�t�| �nddt�� v �st�|��rt�|�ndd	� }d
d|i }tt�|���d }d S )
Nzplz enter valid inputsr)   r,   �valr   r   �	expected3�actual3r    r"   r#   �actual4r$   )r1   r2   r3   r   r%   r&   r   r   r   �test_array_shift_faildtest   s
    
�r4   )�builtinsr   �_pytest.assertion.rewrite�	assertion�rewriter	   Zchallenges.array_shiftr   Z"challenges.array_shift.array_shiftr   r   r'   r/   r4   r   r   r   r   �<module>   s
   &

__init__.cpython-39.py