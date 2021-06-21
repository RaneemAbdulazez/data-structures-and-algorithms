a
�٢`�  �                   @   sb   d dl Zd dlm  mZ d dlmZ dd� Zdd� Z	dd� Z
d	d
� Zdd� Zdd� Zdd� ZdS )�    N)�
LinkedListc                  C   s�   t � } t| t �}|s�ddt�� v s,t�t�r6t�t�nddt�� v sNt�| �rXt�| �nddt�� v spt�t �rzt�t �ndt�|�d� }tt�|���d }d S )Nz5assert %(py4)s
{%(py4)s = %(py0)s(%(py1)s, %(py2)s)
}�
isinstance�llr   )�py0�py1�py2�py4)	r   r   �@py_builtins�locals�
@pytest_ar�_should_repr_global_name�	_saferepr�AssertionError�_format_explanation)r   �@py_assert3�@py_format5� r   �[/home/raneem/codefellows/401/data-structures-and-algorithms/python/tests/test_linkedlist.py�test_instance   s    r   c                  C   s�   t � } | �d� | j}|j}d}||k}|s�t�d|fd||f�dt�� v sVt�| �r`t�	| �ndt�	|�t�	|�t�	|�d� }dd|i }t
t�|���d  } } }}d S )Nr   ��==�zG%(py4)s
{%(py4)s = %(py2)s
{%(py2)s = %(py0)s.head
}.value
} == %(py7)s�test_LinkedList�r   r   r   �py7�assert %(py9)s�py9)r   �insert�head�valuer   �_call_reprcomparer	   r
   r   r   r   r   �r   �@py_assert1r   �@py_assert6�@py_assert5�@py_format8�@py_format10r   r   r   �test_LinkedList_insert
   s    
r'   c            
      C   sn  t � } | �d� | j}|j}d}||k}|s�t�d|fd||f�dt�� v sVt�| �r`t�	| �ndt�	|�t�	|�t�	|�d� }dd|i }t
t�|���d  } } }}| �d� | j}|j}|j}d}||k}|�sVt�d|fd	||f�dt�� v �st�| ��rt�	| �ndt�	|�t�	|�t�	|�t�	|�d
� }dd|i }	t
t�|	���d  } } } }}d S )Nr   r   r   r   r   r   r   �   )za%(py6)s
{%(py6)s = %(py4)s
{%(py4)s = %(py2)s
{%(py2)s = %(py0)s.head
}.next
}.value
} == %(py9)s�r   r   r   �py6r   �assert %(py11)s�py11)r   r   r   r   r   r    r	   r
   r   r   r   r   �next)
r   r"   r   r#   r$   r%   r&   �@py_assert8�@py_assert7�@py_format12r   r   r   �"test_LinkedList_insert_second_Test   s
    
�
r1   c                  C   s�  t � } | �d� | �d� | j}d}||�}d}||k}|s�t�d|fd||f�dt�� v sft�| �rpt�| �ndt�|�t�|�t�|�t�|�d� }dd	|i }t	t�
|���d  } } } }}| j}d
}||�}d}||k}|�sht�d|fd||f�dt�� v �st�| ��r$t�| �ndt�|�t�|�t�|�t�|�d� }dd	|i }t	t�
|���d  } } } }}d S )Nr   r(   Tr   )zN%(py6)s
{%(py6)s = %(py2)s
{%(py2)s = %(py0)s.includes
}(%(py4)s)
} == %(py9)sr   r)   r+   r,   �d   F)r   r   Zincludesr   r    r	   r
   r   r   r   r   )r   r"   r   r$   r.   r/   r&   r0   r   r   r   �test_LinkedList_includes   s
    

�r3   c                  C   s*  t � } | �d� | �d� | �d� | �d� | �d� | �d� | �d� | �d� | �d	� | �d
� | �d� | �d
� | �d� | j}|� }d}||k}|�st�d|fd||f�dt�� v s�t�| �r�t�| �ndt�|�t�|�t�|�d� }dd|i }t	t�
|���d  } } }}d S )N�9�1�-�D�I�V�O�C�_�0�2zy{ 2 } -> { 0 } -> { 2 } -> { 0 } -> { _ } -> { C } -> { O } -> { V } -> { I } -> { D } -> { - } -> { 1 } -> { 9 } -> NULLr   )zF%(py4)s
{%(py4)s = %(py2)s
{%(py2)s = %(py0)s.__str__
}()
} == %(py7)sr   r   r   r   )r   r   �__str__r   r    r	   r
   r   r   r   r   r!   r   r   r   �test__str__!   s    












r@   c                  C   s�   t � } | �d� | �d� | �d� | �d� t| � | �d�}d}||k}|s�t�d|fd||f�dt�� v szt�|�r�t�	|�ndd	t�� v s�t�|�r�t�	|�nd	d
� }dd|i }t
t�|���d }d S )N�   �   �   �raneemr(   r   �z%(py0)s == %(py2)s�	excpected�actual�r   r   �assert %(py4)sr   )r   r   �print�kth_from_the_endr   r    r	   r
   r   r   r   r   �r   rG   rF   r"   �@py_format3r   r   r   r   �test_kthFromEnd3   s    




rN   c                  C   s�   t � } | �d� | �d� | �d� | �d� | �d�}d}||k}|s�t�d|fd||f�d	t�� v srt�|�r|t�|�nd	d
t�� v s�t�|�r�t�|�nd
d� }dd|i }t	t�
|���d }d S )NrA   rB   rC   rD   �   z/Sorry, the value is larger than the linked listr   rE   rF   rG   rH   rI   r   )r   r   rK   r   r    r	   r
   r   r   r   r   rL   r   r   r   �test_kthFromEnd2B   s    




rP   )�builtinsr	   �_pytest.assertion.rewrite�	assertion�rewriter   Z&datastructures.linked_list.linked_listr   r   r'   r1   r3   r@   rN   rP   r   r   r   r   �<module>   s   &