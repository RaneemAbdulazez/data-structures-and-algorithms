a
���`I  �                   @   s�   d dl Zd dlm  mZ d dlmZmZm	Z	m
Z
 d dlZdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Zdd� Zdd� Zejdd� �Zejdd� �ZdS )�    N)�Cat�Dog�AnimalShelter�EmptyQueueExceptionc                  C   s�   d} t d�}t� }|�|� |j� }|| k}|s�t�d|fd|| f�dt�� v sZt�|�rdt�	|�nddt�� v s|t�| �r�t�	| �ndd� }dd|i }t
t�|���d }d S �	N�kitty��==�z%(py0)s == %(py2)s�actual�expected��py0�py2�assert %(py4)s�py4)r   r   �enqueue�cat�
@pytest_ar�_call_reprcompare�@py_builtins�locals�_should_repr_global_name�	_saferepr�AssertionError�_format_explanation)r   �cat1�	animal_shr   �@py_assert1�@py_format3�@py_format5� r!   �d/home/raneem/codefellows/401/data-structures-and-algorithms/python/tests/test_fifo_animal_shelter.py�test_cat_enqueue   s    
r#   c                  C   s�   d} t d�}t� }|�|� |j� }|| k}|s�t�d|fd|| f�dt�� v sZt�|�rdt�	|�nddt�� v s|t�| �r�t�	| �ndd� }dd|i }t
t�|���d }d S )	NZBobir   r
   r   r   r   r   r   )r   r   r   �dogr   r   r   r   r   r   r   r   )r   �dog1r   r   r   r   r    r!   r!   r"   �test_dog_enqueue   s    
r&   c                 C   s�   d}| � }||k}|s�t �d|fd||f�dt�� v s@t �|�rJt �|�nddt�� v sbt �|�rlt �|�ndd� }dd|i }tt �|���d }d S )	Nzkitty lucy sabi radir   r
   r   r   r   r   r   �r   r   r   r   r   r   r   r   ��queue_cat_testr   r   r   r   r    r!   r!   r"   � test_queue__cat_multiple_enqueue   s    r*   c                 C   s�   d}| � }||k}|s�t �d|fd||f�dt�� v s@t �|�rJt �|�nddt�� v sbt �|�rlt �|�ndd� }dd|i }tt �|���d }d S )	Nzbobi sasi soso lulur   r
   r   r   r   r   r   r'   ��queue_dog_testr   r   r   r   r    r!   r!   r"   � test_queue__dog_multiple_enqueue   s    r-   c                 C   s�   d}| � � }||k}|s�t�d|fd||f�dt�� v sBt�|�rLt�|�nddt�� v sdt�|�rnt�|�ndd� }dd|i }tt�|���d }d S r   �	�dequeuer   r   r   r   r   r   r   r   r(   r!   r!   r"   �test_queue_cat_dequeue   s    r0   c                 C   s�   d}| � � }||k}|s�t�d|fd||f�dt�� v sBt�|�rLt�|�nddt�� v sdt�|�rnt�|�ndd� }dd|i }tt�|���d }d S )	N�bobir   r
   r   r   r   r   r   r.   r+   r!   r!   r"   �test_queue_dog_dequeue$   s    r2   c                 C   sL   t d�D ]}| ��  qt�t�� | ��  W d   � n1 s>0    Y  d S �N�   ��ranger/   �pytest�raisesr   )r)   �numr!   r!   r"   �test_queue_cat_multiple_dequeue*   s    
r:   c                 C   sL   t d�D ]}| ��  qt�t�� | ��  W d   � n1 s>0    Y  d S r3   r5   )r,   r9   r!   r!   r"   �test_queue_dog_multiple_dequeue0   s    
r;   c                  C   sT   t d�} t d�}t d�}t d�}t� }|�| � |�|� |�|� |�|� |jS )Nr   ZlucyZsabiZradi)r   r   r   r   )r   Zcat2Zcat3Zcat4r   r!   r!   r"   r)   7   s    



r)   c                  C   sT   t d�} t d�}t d�}t d�}t� }|�| � |�|� |�|� |�|� |jS )Nr1   ZsasiZsosoZlulu)r   r   r   r$   )r%   Zdog2Zdog3Zdog4r   r!   r!   r"   r,   F   s    



r,   )�builtinsr   �_pytest.assertion.rewrite�	assertion�rewriter   Z2challenges.fifo_animal_shelter.fifo_animal_shelterr   r   r   r   r7   r#   r&   r*   r-   r0   r2   r:   r;   �fixturer)   r,   r!   r!   r!   r"   �<module>   s   2
