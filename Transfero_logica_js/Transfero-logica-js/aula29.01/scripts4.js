let resposta = prompt("Olá muito bem vindo ao sistema do DETRAN!\n 1- Prosseguir\n 2- Cancelar");
switch (resposta){
    case "1":
        let nome = prompt("Qual é o seu nome: ");
        let idade = parseFloat(prompt("Qual a sua idade: "));
        if(idade > 18){
            document.write("Olá muito bem vindo! " + nome + "\n Você é maior de idade. \n Portanto você poderá dirigir!");
        
        } else {
            document.write("Olá muito bem vindo! " + nome + "\n Você é menor de idade. \n Portanto você não poderá dirigir!");
        }
        break;
        case "2":
        document.write("Operação cancelada!");
        break;
        default:
            document.write("Valor inválido! \n Cancelando a operação. . .")
}