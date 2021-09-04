<template>
  <div id="app">
    <Form />
    <Footer />
  </div>
</template>

<script>
import Form from "./components/Form.vue";
import Footer from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    Form,
    Footer,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
