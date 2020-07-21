## Código

```c#
List<int> lista = new List<int>();
int i = 0;
for(i; i<200; i++){
	bool cond = lista.Contains(i);
	if(!cond){
		for(int j=0; j<20; j++){
			lista.Add(i*j);
		}	
	}else{
		lista.Add(i);
	}
}
var lista2 = lista.GetRange(0, 5);
HashSet<string> conjunto = new HashSet<string>();
string cadena = "C# es el mejor lenguaje de programación";
int cont = 0;
int pos = 0;
string espacio = ' ';
while(cont < 39){
	var caracter = cadena[cont];
	if(caracter == espacio){
		string value = cadena.Substring(pos, cont-1);
		conjunto.Add(value);
		pos += cont;	
	}
	cont++;
}
Console.WriteLine("Factorial");
var end = Console.ReadLine();
int fact = 1;
for(int i=1; i<=end; i++){
	fact = fact * i;
}
Console.WriteLine("El factorial es: ");
Console.WriteLine(fact);
int valor = 21;
string texto = "Hola Mundo";
var tupla = (nombre: nombre, valor: valor);
int dato = tupla.Item2 + 1;
HashSet<int> set = new HashSet<int>();
set.Add(456);
set.Add(345);
set.Add(42);
HashSet<int> cojunto= new HashSet<int>();
set.Add(456);
set.UnionWith(conjunto);
```