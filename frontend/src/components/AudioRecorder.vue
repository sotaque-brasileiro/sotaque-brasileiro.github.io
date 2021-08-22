<template>
  <span>
    <div class="col-xs-12">
      <div class="row">
        <h4>Grave sua voz dizendo a seguinte frase:</h4>
        <h2>{{ message }}</h2>
      </div>
      <div class="row">
        <vue-record-audio @result="onResult" />
      </div>
    </div>
    <div v-if="this.audioBlob" class="col-md-12 col-xs-12">
      <h4>Confira a sua gravação aqui:</h4>
      <audio :src="audioSrc" type="audio/wav" controls></audio>
    </div>
  </span>
</template>

<script>
import VueRecord from "@codekraft-studio/vue-record";
import Vue from "vue";
import { mapState } from "vuex";

Vue.use(VueRecord);

export default {
  methods: {
    onResult(data) {
      this.audioBlob = data;
      this.$store.dispatch("form/setAudioBlob", data);
    },
  },
  data() {
    return {
      audioSrc: null,
      audioBlob: null,
      message:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempor",
    };
  },
  props: {
    model: {
      type: Object,
      required: true,
    },
  },
  computed: {
    ...mapState({
      store_audio_blob: (state) => state.form.audioBlob,
    }),
  },
  watch: {
    store_audio_blob: {
      handler(newVal) {
        if (newVal == null) {
          this.audioSrc = null;
          this.audioBlob = null;
        } else {
          this.audioSrc = URL.createObjectURL(newVal);
        }
      },
    },
  },
};
</script>

<style>
</style>