A = int(input("Informe um valor numérico: "))
B = int(input("Informe um valor numérico: "))
C = int(input("Informe um valor numérico: "))

if A<B and A<C and B<C:
    print(f"{A},{B},{C}")
elif A<B and A<C and C<B:
    print(f"{A},{C},{B}")
elif B<A and B<C and C<A:
    print(f"{B},{C},{A}")
elif B<A and B<C and A<C:
    print(f"{B},{A},{C}")
elif C<A and C<B and A<B:
    print(f"{C},{A},{B}")
elif C<A and C<B and B<A:
    print(f"{C},{B},{A}")