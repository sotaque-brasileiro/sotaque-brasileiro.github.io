<template>
  <div class="col-xs-12">
    <p>
      Na próxima etapa, você poderá iniciar as gravações de áudio. Escolha, de
      preferência, um ambiente silencioso ou com pouco ruído, para tentar
      adquirir a melhor qualidade de áudio possível. Assim que abrir, você verá
      uma frase e um botão para iniciar a gravação, como na imagem abaixo:
    </p>
    <img src="../assets/acc01.png" class="img-responsive" />
    <p>
      Você poderá iniciar a gravação clicando e segurando o botão. Assim que
      você iniciar a gravação, ele mudará de cor para vermelho e será escrito
      "Gravando", como a imagem abaixo. Caso o botão não fique vermelho, você
      deve permitir o acesso à gravação de áudio, que deve estar bloqueado.
    </p>
    <img src="../assets/acc02.png" class="img-responsive" />
    <p>
      Quando você terminar a gravação, basta soltar o botão para parar a
      gravação. Assim que o fizer, ele mudará de cor para verde e será exibido
      um reprodutor de áudio, para que você possa conferir o que foi gravado.
    </p>
    <img src="../assets/acc03.png" class="img-responsive" />
    <p>
      Caso o áudio esteja de acordo com o esperado, você poderá clicar no botão
      "Enviar" para enviar o áudio para o servidor. Assim que você clicar, uma
      mensagem de confirmação será exibida. Caso o áudio esteja incorreto, você
      poderá regravá-lo, clicando novamente no mesmo botão.
    </p>
    <img src="../assets/acc04.png" class="img-responsive" />
    <p>
      Quando clicar em "Ok" na mensagem de confirmação, outra frase será
      exibida. Você poderá gravar quantas quiser. Quando quiser parar, é só
      fechar essa janela.
    </p>
    <img src="../assets/acc05.png" class="img-responsive" />
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
img {
  border: 5px solid #555;
}
.img-responsive {
  margin: 0 auto;
}
</style>