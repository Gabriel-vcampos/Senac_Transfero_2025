let optionofgame = parseFloat(prompt("Bem vindo ao pedra, papel e tesoura\n Digite \n 1: Pedra \n 2- Tesoura \n 3-Papel"));

switch (optionofgame) {
        case 1:
        document.write("Opção escolhida do jogador: Pedra \n");
        break;
        case 2:
            document.write("Opção escolhida do jogador: Tesoura \n");
            break;
        case 3:
            document.write("Opção escolhida do jogador: Papel \n");
            break;
        default:
            document.write("Opção inexistente. Tente novamente! \n");
            break;
}
let computerchoice = ["pedra", "tesoura", "papel"];
let escolha = computerchoice[Math.floor(Math.random() * 3)];

  document.write("<br>" + "A opção escolhida da máquina foi:" +resultado)
if(optionofgame == computerchoice[escolha-1]){}

