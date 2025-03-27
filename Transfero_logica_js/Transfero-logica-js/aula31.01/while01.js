let numero = parseFloat(prompt("Digite um número que irei fazer uma contagem progressiva do número respondido até o 10"))
if(isNaN(numero)){
    document.write("O valor não é um número!");
} else {
while (numero <= 10){
    document.write(numero + "<br>");
    numero++;
 }
}