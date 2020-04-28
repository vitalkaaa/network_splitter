Write source network ranges one on line then empty string and then network ranges for excluding

For example fill input.txt like there:

input.txt
---------
1.0.0.0/24
2.0.0.0/24

1.0.0.128/32

3) As result you will get output.txt

output.txt
----------
1.0.0.0-1.0.0.127
1.0.0.129-1.0.0.255
2.0.0.0-2.0.0.255