def main():
    #escribe tu código abajo de esta línea
    n=int(input())
    c=1
    suma=0
    numero=0
    while c<=n:
        numero=float(input())
        suma+=numero
        promedio=suma/n
        c+=1
    print(promedio)

        
if __name__=='__main__':
    main()
