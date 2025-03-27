let peso = parseFloat(prompt("Qual é o peso do indivíduo: "));
let altura = parseFloat(prompt("Qual é a altura do indivíduo: "));

let IMC = peso / (altura * altura);

if (IMC < 18.5) {
    alert("Você está abaixo do peso.");
} else if (IMC >= 18.5 && IMC < 25) {
    alert("Você está no peso ideal.");
} else if (IMC >= 25 && IMC < 30) {
    alert("Você está acima do peso ideal.");
} else if (IMC >= 30 && IMC < 35) {
    alert("Você está em obesidade grau I.");
} else if (IMC >= 35 && IMC < 40) {
    alert("Você está em obesidade grau II.");
} else {
    alert("Você está em obesidade grau III.");
}

console.log("IMC: " + IMC);