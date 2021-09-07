<template>
  <span>
    <div class="col-xs-12">
      <div class="row">
        <h4>Grave sua voz dizendo a seguinte frase:</h4>
        <h2>{{ store_sentence }}</h2>
      </div>
      <div class="row">
        <vue-record-audio
          :mode="`hold`"
          @result="onResult"
          @stream="onStream"
        />
      </div>
    </div>
    <div v-if="record_state !== `granted`" class="col-md-12 col-xs-12">
      <h4>Para gravar sua voz, você precisa permitir o uso de microfone.</h4>
    </div>
    <div v-if="recording" class="col-md-12 col-xs-12">
      <h4>Gravando...</h4>
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
      this.recording = false;
      this.audioBlob = data;
      this.$store.dispatch("form/setAudioBlob", data);
    },
    onStream() {
      this.recording = true;
    },
  },
  data() {
    return {
      audioSrc: null,
      audioBlob: null,
      recording: false,
      recordState: "",
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
      store_sentence: (state) => state.form.sentence,
      record_state: (state) => state.form.recordState,
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
  mounted() {
    this.$store.dispatch("form/fetchRecordState");
  },
};
</script>

<style>
</style>