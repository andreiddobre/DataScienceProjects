3 Main Properties Of The Einstein Summation
There are three main properties of the Einstein summation that is used in advanced mathematics and physics for brevity.

They are:

-Summation is carried over for indices that are repeated

-The limit for the appearance of each index is two

-Each term of the Einstein Summation can at most have two identical index

Syntax Of The Numpy.Einsum() Function
The einsum() function is written in the following manner:

numpy.einsum(subscripts, *operands, out, dtype, order, casting, optimize)

The parameters of the function are:

subscripts: string type ->specifies the list for comma separated subscripts when explicitly mentioned with the “->” sign. Otherwise, implicitly the classical Einstein Summation is calculated.
*operands: ndarray ->The arrays which are operated on.
out: ndarray-> (optional) If specified the Einstein summation is stored in this array.
dtype: data type-> (optional) If specified, forces the calculation to limit itself to a specified data type. The default value of this parameter is None.
order:{'C','F','A','K'}-> (optional) Determines the output’s memory structure . C= contiguous, F= Fortran contiguous, K=the same layout as the inputs and A= ‘F’ if inputs are all ‘F’ and ‘C’ otherwise.
casting{‘no’, ‘safe’, ‘unsafe’,‘equiv’,‘same_kind’}->optional Determines the type of casting that might occur with the data. ‘no’ means there should be no casting, ‘safe’ means the allowed values should be preserve, ‘unsafe’ ( not recommended) means all kinds of conversion is allowed, ‘equiv’ allows only byte-sized changes and ‘same_kind’ represents that only certain kind of casting such as float64 or float32 should be allowed. When not mentioned, the default is ‘safe’.
optimize{'optimal','greedy',True,False}->(optional) no optimization of intermediate resources occur if set to False, but when set to True, it will take up the default ‘greedy’ value.
The output of the function is:

Output: ndarray -> The Einstein Summation is returned.
