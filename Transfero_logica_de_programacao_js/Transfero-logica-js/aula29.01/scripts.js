let valor1 = parseFloat(prompt("Digite um valor:"));
let valor2 = parseFloat(prompt("Digite outro valor:"));
let resultado = valor1 + valor2

if(isNaN(resultado)){
    document.write("O valor está inválido!");
} else {
    document.write("A soma entre os 2 números é:" + resultado);
if(resultado > 20){
    document.writeln("<br>O resultado é maior ou igual a 20.");
} else if(resultado <20) {
    document.writeln("<br>O resultado é menor que 20.");
} else {
    document.writeln("<br>O resultado é igual a 20.");  
}
}