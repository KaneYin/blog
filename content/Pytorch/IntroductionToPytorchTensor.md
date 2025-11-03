Tensors are the central data abstraction in PyTorch. This interactive notebook provides an indepth introduction to the `torch.tensor` class.

Tensors are similar to NumPy’s ndarrays, except that tensors can run on GPUs or other hardware accelerators. In fact, tensors and NumPy arrays can often share the same underlying memory, eliminating the need to copy data. Tensors are also optimized for automatic differentiation (we’ll see more about that later in the Autograd section). If you’re familiar with ndarrays, you’ll be right at home with the Tensor API. If not, follow along!

First things first, let’s import the PyTorch module. We’ll also add Python’s math module to facilitate some of the examples.


```python
# pip install torch
```

    Collecting torch
      Using cached torch-2.9.0-cp313-none-macosx_11_0_arm64.whl.metadata (30 kB)
    Requirement already satisfied: filelock in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from torch) (3.19.1)
    Requirement already satisfied: typing-extensions>=4.10.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from torch) (4.15.0)
    Requirement already satisfied: setuptools in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from torch) (80.9.0)
    Collecting sympy>=1.13.3 (from torch)
      Using cached sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
    Collecting networkx>=2.5.1 (from torch)
      Using cached networkx-3.5-py3-none-any.whl.metadata (6.3 kB)
    Requirement already satisfied: jinja2 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from torch) (3.1.6)
    Collecting fsspec>=0.8.5 (from torch)
      Using cached fsspec-2025.9.0-py3-none-any.whl.metadata (10 kB)
    Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch)
      Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
    Requirement already satisfied: MarkupSafe>=2.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from jinja2->torch) (3.0.3)
    Using cached torch-2.9.0-cp313-none-macosx_11_0_arm64.whl (74.5 MB)
    Using cached fsspec-2025.9.0-py3-none-any.whl (199 kB)
    Using cached networkx-3.5-py3-none-any.whl (2.0 MB)
    Using cached sympy-1.14.0-py3-none-any.whl (6.3 MB)
    Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
    Installing collected packages: mpmath, sympy, networkx, fsspec, torch
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m5/5[0m [torch]32m4/5[0m [torch]]x]
    [1A[2KSuccessfully installed fsspec-2025.9.0 mpmath-1.3.0 networkx-3.5 sympy-1.14.0 torch-2.9.0
    
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip is available: [0m[31;49m25.2[0m[39;49m -> [0m[32;49m25.3[0m
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpip install --upgrade pip[0m
    Note: you may need to restart the kernel to use updated packages.



```python
import torch
import math
```

# Creating Tensors
The simplest way to create a tensor is with the `torch.empty()` call:


```python
x = torch.empty(3, 4)
print(type(x))
print(x)
```

    <class 'torch.Tensor'>
    tensor([[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]])


Let’s upack what we just did:
- We created a tensor using one of the numerous factory methods attached to the torch module.
- The tensor itself is 2-dimensional, having 3 rows and 4 columns.
- The type of the object returned is torch.Tensor, which is an alias for torch.FloatTensor; by default, PyTorch tensors are populated with 32-bit floating point numbers. (More on data types below.)

A brief note about tensors and their number of dimensions, and terminology:
- You will sometimes see a 1-dimensional tensor called a vector.
- Likewise, a 2-dimensional tensor is often referred to as a matrix.
- Anything with more than two dimensions is generally just called a tensor.
 


```python
zeros = torch.zeros(2, 3)
print(zeros)

ones = torch.ones(2, 3)
print(ones)

torch.manual_seed(1729)
random = torch.rand(2, 3)
print(random)
```

    tensor([[0., 0., 0.],
            [0., 0., 0.]])
    tensor([[1., 1., 1.],
            [1., 1., 1.]])
    tensor([[0.3126, 0.3791, 0.3087],
            [0.0736, 0.4216, 0.0691]])


Speaking of the random tensor, did you notice the call to `torch.manual_seed()` immediately preceding it? Initializing tensors, such as a model’s learning weights, with random values is common but there are times - especially in research settings - where you’ll want some assurance of the reproducibility of your results. Manually setting your random number generator’s seed is the way to do this. Let’s look more closely.

What you should see above is that `random1` and `random3` carry identical values, as do `random2` and `random4`. Manually setting the RNG’s seed resets it, so that identical computations depending on random number should, in most settings, provide identical results.


```python
torch.manual_seed(1729)
random1 = torch.rand(2, 3)
print(random1)

random2 = torch.rand(2, 3)
print(random2)

torch.manual_seed(1729)
random3 = torch.rand(2, 3)
print(random3)

random4 = torch.rand(2, 3)
print(random4)
```

# Tensor Data Types
Setting the datatype of a tensor is possible a couple of ways:


```python
a = torch.ones((2, 3), dtype=torch.int16)
print(a)

b = torch.rand((2, 3), dtype=torch.float64) * 20
print(b)

c = b.to(torch.int32)
print(c)
```

    tensor([[1, 1, 1],
            [1, 1, 1]], dtype=torch.int16)
    tensor([[17.3151, 14.5980,  6.0404],
            [18.0429,  7.2532, 19.6519]], dtype=torch.float64)
    tensor([[17, 14,  6],
            [18,  7, 19]], dtype=torch.int32)


The simplest way to set the underlaying data type of a tensor is with an optional argument at creation time. In the first line of the cell above, we set `dtype=torch.int16` for the tensor `a`. When we print `a`, we can see that it’s full of 1 rather than 1. - Python’s subtle cue that this is an integer type rather than floating point


Another thing to notice about printing `a` is that, unlike when we left `dtype` as the default (32-bit floating point), printing the tensor also specifies its `dtype`.



# Tensor Shapes
Often, when you're performing operations on tow or more tensors, they will need to be of the same shape - that is, having the same number of dimensions and the same number of cells in each dimension. For that, we have the `torch.*_like()` methods:

The `.shape` property contains a list of the extent of each dimension of a tensor - in our case, `x` is a three dimensional tensor with shape 2*2*3.

Below that, we call the `.empty_like()`, `.zeros_like()`, `.ones_like()`, and `.rand_like()` methods. Using the `.shape` property, we can verify that each of these methods returns a tensor of identical dimensionality and extent.


```python
x = torch.empty(2, 2, 3)
print(x.shape)
print(x)

empth_like_x = torch.empty_like(x)
print(empth_like_x.shape)
print(empth_like_x)

ones_like_x = torch.ones_like(x)
print(ones_like_x.shape)
print(ones_like_x)

```

    torch.Size([2, 2, 3])
    tensor([[[0., 0., 0.],
             [0., 0., 0.]],
    
            [[0., 0., 0.],
             [0., 0., 0.]]])
    torch.Size([2, 2, 3])
    tensor([[[0., 0., 0.],
             [0., 0., 0.]],
    
            [[0., 0., 0.],
             [0., 0., 0.]]])
    torch.Size([2, 2, 3])
    tensor([[[1., 1., 1.],
             [1., 1., 1.]],
    
            [[1., 1., 1.],
             [1., 1., 1.]]])


# Math & Logic with PyTorch Tensors

Now we have know some of ways to create a tensor. What we can do with them?
Let's look at basic arithmetic first, and how tensors interact with simple scalars:



```python
ones = torch.zeros(2, 2) + 1
twos = torch.ones(2, 2) * 2
threes = (torch.ones(2, 2) * 7 - 1) / 2
fours = twos ** 2
sqrt2s = twos  ** 0.5

print(ones)
print(twos)
print(threes)
print(fours)
print(sqrt2s)
```

    tensor([[1., 1.],
            [1., 1.]])
    tensor([[2., 2.],
            [2., 2.]])
    tensor([[3., 3.],
            [3., 3.]])
    tensor([[4., 4.],
            [4., 4.]])
    tensor([[1.4142, 1.4142],
            [1.4142, 1.4142]])


As you can see above, arithmetic operations between tensors and scalars, such as addition, substraction, multiplication, division, and exponentiation are distributed over every element of the tensor. Because the output of such an operation will be a tensor, you can chain them together with the usual operator precedence rules, as in the line where we create threes.

Similiar operations:


```python
powers2 = twos ** torch.tensor([[1, 2], [3, 4]])
print(powers2)

fives = ones + fours
print(fives)

dozens = threes * fours
print(dozens)

```

    tensor([[ 2.,  4.],
            [ 8., 16.]])
    tensor([[5., 5.],
            [5., 5.]])
    tensor([[12., 12.],
            [12., 12.]])


# Copying Tensors
As with any object in Python, assigning a tensor to a variable makes the variable a label of the tensor, and does not copy it. For example:



```python
a = torch.ones(2, 2)
b = a

a[0][1] = 561
print(b)
```

    tensor([[  1., 561.],
            [  1.,   1.]])


But what if you want a separate copy of the data to work on? The `clone()` method is there for you.


```python
a = torch.ones(2, 2)
b = a.clone()

assert b is not a
print(torch.eq(a, b))

a[0][1] = 256
print(b)
```

    tensor([[True, True],
            [True, True]])
    tensor([[1., 1.],
            [1., 1.]])


There is something important to be aware of when using 'clone()'. If your source tensor has autograd, the cloned tensor will also have the autograd. 

## light version of the autograd
In many cases, this will be what you want. For example,  if your model has multiple computation paths in its `forward()` method, and both the original tensor and its clone contribute to the model's output, then to enable model learning you want autograd turned on for both tensors. If your source tensor has autograd enabled (which it generally will if it's a set of learning weights or derived from a computtation involving the weights), then you'll get the result you want.

On the other hand, if you’re doing a computation where neither the original tensor nor its clone need to track gradients, then as long as the source tensor has autograd turned off, you’re good to go.

There is a third case, though: Imagine you’re performing a computation in your model’s forward() function, where gradients are turned on for everything by default, but you want to pull out some values mid-stream to generate some metrics. In this case, you don’t want the cloned copy of your source tensor to track gradients - performance is improved with autograd’s history tracking turned off. For this, you can use the .detach() method on the source tensor:



```python
a = torch.rand(2, 2, requires_grad = True)
print(a)

b = a.clone()
print(b)

c = a.detach().clone()
print(c)

print(a)
```

    tensor([[0.7433, 0.5816],
            [0.4171, 0.9898]], requires_grad=True)
    tensor([[0.7433, 0.5816],
            [0.4171, 0.9898]], grad_fn=<CloneBackward0>)
    tensor([[0.7433, 0.5816],
            [0.4171, 0.9898]])
    tensor([[0.7433, 0.5816],
            [0.4171, 0.9898]], requires_grad=True)


What’s happening here?

We create `a` with `requires_grad=True` turned on. We haven’t covered this optional argument yet, but will during the unit on autograd.
When we print `a`, it informs us that the property `requires_grad=True` - this means that autograd and computation history tracking are turned on.
We clone `a` and label it `b`. When we print `b`, we can see that it’s tracking its computation history - it has inherited a’s autograd settings, and added to the computation history.
We clone a into c, but we call `detach()` first.
Printing c, we see no computation history, and no `requires_grad=True`.
The `detach()` method detaches the tensor from its computation history. It says, “do whatever comes next as if autograd was off.” It does this without changing a - you can see that when we print a again at the end, it retains its requires_grad=True property.

# Moving to Accelerator
One of the major advantages of PyTorch is its robust acceleration on an accelerator such as CUDA. So far, everything we've done has been on CPU. How do we move to the faster hardware?

First, we should check whether an accelerator is available, with `is_available()` method.


```python
if torch.accelerator.is_available():
    print("We have an accelerator!")
else:
    print("Sorry, CPU only.")
```

    We have an accelerator!


Once we’ve determined that one or more accelerators is available, we need to put our data someplace where the accelerator can see it. Your CPU does computation on data in your computer’s RAM. Your accelerator has dedicated memory attached to it. Whenever you want to perform a computation on a device, you must move all the data needed for that computation to memory accessible by that device.

There are multiple ways to get your data onto your target device. You may do it at creation time:


```python
if torch.accelerator.is_available():
    gpu_rand = torch.rand(2, 2, device=torch.accelerator.current_accelerator())
    print(gpu_rand)
else:
    print('Sorry, CPU only.')
```

    tensor([[0.2172, 0.3683],
            [0.0173, 0.0119]], device='mps:0')


By default, new tensors are created on the CPU, so we have to specify when we want to create our tensor on the accelerator with the optional `device` argument. You can see when we print the new tensor, PyTorch informs us which device it’s on (if it’s not on CPU).


```python
my_device = torch.accelerator.current_accelerator() if torch.accelerator.is_available() else torch.device('cpu')
print('Device: {}'.format(my_device))

x = torch.rand(2, 2, device=my_device)
print(x)
```

# Manipulating Tensor Shapes

Sometimes, you'll need to change the shape of your tensor. Below, we'll took at a few common cases, and how to handle them.


