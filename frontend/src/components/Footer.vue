<template>
  <div id="container">
    <div id="mentions" class="col-xs-12 col-md-9 col-xl-6">
      <p>
        <b>[1]</b> BATISTA, Nathalia Alves Rocha.
        <b
          >Estudo sobre Identificação Automática de Sotaques Regionais
          Brasileiros baseada em Modelagens Estatísticas e Técnicas de
          Aprendizado de Máquina</b
        >. 2019. Dissertação (Mestrado em Engenharia Elétrica) - Faculdade de
        Engenharia Elétrica e de Computação da Universidade Estadual de
        Campinas, [<i>S. l.</i>], 2019. Disponível em:
        http://repositorio.unicamp.br/jspui/bitstream/REPOSIP/334048/1/Batista_NathaliaAlvesRocha_M.pdf.
        Acesso em: 4 set. 2021.
      </p>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Open+Sans");

body {
  display: flex;
  background-color: #f0f8ff;
  height: 95vh;
  justify-content: center;
  align-items: flex-end;
  font-family: Open Sans;
}

#container {
  padding-top: 20px;
  margin-top: 20px;
  width: 100vw;
  color: white;
  background-color: #292354;
  display: flex;
  flex-direction: column;
  align-items: center;
}
#contacts {
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 100%;
}
#contacts--contact {
  text-align: right;
}
#contacts--social {
  width: 20%;
  display: flex;
  justify-content: space-between;
}
#contacts--social div {
  height: 30px;
  width: 30px;
  background-color: white;
  border-radius: 50%;
}
#mentions p {
  font-size: 1em;
}
p {
  word-break: break-word;
}
</style>