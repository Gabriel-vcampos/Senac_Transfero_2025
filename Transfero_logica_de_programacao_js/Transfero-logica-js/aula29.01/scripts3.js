let lado_1_triangulo = parseFloat(prompt("Digite um lado do triângulo: "));
let lado_2_triangulo = parseFloat(prompt("Digite outro lado do triângulo: "));
let lado_3_triangulo = parseFloat(prompt("Digite outro lado do triângulo: "));

if(isNaN(lado_1_triangulo) || isNaN(lado_2_triangulo) || isNaN(lado_3_triangulo)){
    document.write("Erro! Você não inseriu algum dado do lado do triângulo!")
} else {
    if(lado_1_triangulo + lado_2_triangulo < lado_3_triangulo) {
    document.write("Os lados fornecidos não formam um triângulo.");
} else if (lado_2_triangulo + lado_3_triangulo < lado_1_triangulo){;
    document.write("Os lados fornecidos não formam um triângulo.");
}else if (lado_1_triangulo + lado_3_triangulo < lado_2_triangulo){
        document.write("Os lados fornecidos não formam um triângulo.");
    } else {
        if(lado_1_triangulo == lado_2_triangulo && lado_2_triangulo == lado_3_triangulo) {
            document.write("Os lados formam um triângulo equilátero.");
        } else if(lado_1_triangulo == lado_2_triangulo || lado_1_triangulo == lado_3_triangulo || lado_2_triangulo == lado_3_triangulo) {
            document.write("Os lados formam um triângulo isósceles."); 
        } else {
            document.write("Os lados formam um triângulo escaleno.");
        }
    }
}