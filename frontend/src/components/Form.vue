<template>
  <form-wizard
    @on-complete="onComplete"
    color="green"
    error-color="#a94442"
    title="Lorem ipsum"
    subtitle="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempor."
    back-button-text="Voltar"
    next-button-text="Avançar"
    finish-button-text="Enviar"
  >
    <tab-content
      title="Introdução"
      :before-change="validateIntroductionTab"
      icon="ti-info-alt"
    >
      <div class="container h-100">
        <vue-form-generator
          :model="model"
          :schema="introductionTabSchema"
          :options="formOptions"
          ref="introductionTab"
        ></vue-form-generator>
      </div>
    </tab-content>
    <tab-content
      title="Coleta de informações"
      :before-change="validatePersonalInformationTab"
      icon="ti-user"
    >
      <div class="container h-100">
        <vue-form-generator
          :model="model"
          :schema="personalInformationTabSchema"
          :options="formOptions"
          ref="personalInformationTab"
        ></vue-form-generator>
      </div>
    </tab-content>
    <tab-content title="Instruções para as gravações" icon="ti-help-alt">
      <div class="container h-100">
        <RecordInstructions />
      </div>
    </tab-content>
    <tab-content title="Gravações" icon="ti-microphone">
      <div class="container h-100">
        <AudioRecorder :model="model" />
        <div style="display: inline-block">
          <div style="position: relative; margin: auto auto auto auto">
            <vue-recaptcha
              ref="recaptcha"
              @verify="onCaptchaVerified"
              @expired="onCaptchaExpired"
              size="invisible"
              sitekey="6LcIfxocAAAAANzwga4Y1d_HLwrYbQJLlxgENqsU"
            >
            </vue-recaptcha>
          </div>
        </div>
      </div>
    </tab-content>
  </form-wizard>
</template>

<script>
import Vue from "vue";
import { FormWizard, TabContent } from "vue-form-wizard";
import VueFormGenerator from "vue-form-generator";
import "vue-form-wizard/dist/vue-form-wizard.min.css";
import "vue-form-generator/dist/vfg.css";
import AudioRecorder from "./AudioRecorder.vue";
import RecordInstructions from "./RecordInstructions.vue";
import VueRecaptcha from "vue-recaptcha";
import config from "../config";
import { mapState } from "vuex";

Vue.use(VueFormGenerator);

export default {
  components: {
    FormWizard,
    TabContent,
    AudioRecorder,
    RecordInstructions,
    VueRecaptcha,
  },
  computed: mapState({
    store_model: (state) => state.form.model,
    store_audio_blob: (state) => state.form.audioBlob,
    store_gender_list: (state) => state.form.genderList,
    store_city_list: (state) => state.form.cityList,
  }),
  mounted() {
    this.$store.dispatch("form/fetchGenderList");
    this.$store.dispatch("form/fetchCityList");
  },
  watch: {
    store_gender_list: {
      handler(newVal) {
        if (!(newVal == null)) {
          this.personalInformationTabSchema.fields[1].values = newVal;
        }
      },
    },
    store_city_list: {
      handler(newVal) {
        if (!(newVal == null)) {
          this.personalInformationTabSchema.fields[3].values = newVal;
          this.personalInformationTabSchema.fields[4].values = newVal;
          this.personalInformationTabSchema.fields[6].values = newVal;
        }
      },
    },
  },
  data() {
    return {
      model: {
        accept_terms: true,
        age: 24,
        gender: "Masculino",
        profession: "Engenheiro de Dados",
        birth_city: "Americana/SP",
        current_city: "Rio de Janeiro/RJ",
        years_on_current_city: 6,
        parents_original_city: "Turmalina/SP",
      },
      formOptions: {
        validationErrorClass: "has-error",
        validationSuccessClass: "has-success",
        validateAfterChanged: true,
      },
      introductionTabSchema: {
        fields: [
          {
            type: "label",
            label:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ullamcorper \
              dictum euismod. Aenean convallis molestie quam vitae accumsan. Integer \
              quis nunc vel lectus venenatis suscipit. Vivamus aliquam, turpis sit amet \
              vehicula congue, diam ligula ultrices nunc, et ullamcorper ligula ex in \
              velit. Ut dignissim tortor in ex tincidunt, at aliquet dolor consequat. \
              Suspendisse eu ligula eu mi pellentesque vestibulum. Orci varius natoque \
              penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer \
              enim lorem, feugiat a sodales sagittis, porttitor sit amet quam. Nam \
              accumsan molestie nulla, vitae porttitor lorem. Vestibulum molestie \
              placerat facilisis. Maecenas pharetra feugiat quam, eget faucibus ligula \
              varius sit amet. In vitae enim malesuada, gravida ante a, elementum leo. \
              Proin vel metus ex. Morbi tristique sit amet ex sit amet auctor.",
          },
          {
            type: "checkbox",
            label: "Eu li e aceito as condições descritas acima",
            model: "accept_terms",
            required: true,
            validator: (value) => {
              if (value === false) {
                return "Você deve aceitar as condições para continuar.";
              }
            },
          },
        ],
      },
      personalInformationTabSchema: {
        fields: [
          {
            type: "input",
            inputType: "number",
            label: "Qual a sua idade?",
            model: "age",
            required: true,
            styleClasses: "col-md-6 col-xs-12",
            validator: (value) => {
              if (!value) {
                return "Você deve informar sua idade.";
              } else if (value < 1 || value > 120) {
                return "Sua idade deve estar entre 1 e 120 anos.";
              }
            },
          },
          {
            type: "select",
            label: "Qual seu gênero?",
            model: "gender",
            required: true,
            values: ["Carregando..."],
            styleClasses: "col-md-6 col-xs-12",
            validator: (value) => {
              if (!value) {
                return "Você deve selecionar uma das opções de gênero";
              }
            },
          },
          {
            type: "input",
            inputType: "text",
            label: "Qual sua profissão?",
            model: "profession",
            required: false,
            styleClasses: "col-md-6 col-xs-12",
          },
          {
            type: "select",
            label: "Em que cidade você nasceu?",
            model: "birth_city",
            required: true,
            values: ["Carregando..."],
            styleClasses: "col-md-6 col-xs-12",
            validator: (value) => {
              if (!value) {
                return "Você deve informar a cidade onde nasceu.";
              }
            },
          },
          {
            type: "select",
            label: "Em qual cidade você mora atualmente?",
            model: "current_city",
            required: true,
            values: ["Carregando..."],
            styleClasses: "col-md-6 col-xs-12",
            validator: (value) => {
              if (!value) {
                return "Você deve informar a cidade onde mora atualmente.";
              }
            },
          },
          {
            type: "input",
            inputType: "number",
            label: "Há quantos anos você mora nessa cidade?",
            model: "years_on_current_city",
            required: true,
            styleClasses: "col-md-6 col-xs-12",
            validator: (value) => {
              if (!value) {
                return "Você deve informar há quantos anos mora nessa cidade.";
              } else if (value < 0 || value > 120) {
                return "O tempo em que você mora na cidade deve estar entre 0 e 120 anos.";
              }
            },
          },
          {
            type: "select",
            inputType: "select",
            label:
              "Em que cidade seus pais nasceram? Caso sejam de cidades diferentes, informe apenas uma de sua escolha.",
            model: "parents_original_city",
            required: true,
            values: ["Carregando..."],
            styleClasses: "col-md-6 col-xs-12",
            validator: (value) => {
              if (!value) {
                return "Você deve informar a cidade onde seus pais nasceram.";
              }
            },
          },
        ],
      },
    };
  },
  methods: {
    onComplete() {
      if (this.store_audio_blob == null) {
        alert("Você deve gravar um áudio antes de enviar!");
        return;
      }
      if (!this.store_model.accept_terms) {
        alert("Você deve aceitar as condições para continuar.");
        return;
      }
      this.$refs.recaptcha.execute();
      // alert("Nice mlk!");
    },
    onCaptchaVerified: function (recaptchaToken) {
      this.$refs.recaptcha.reset();
      var fd = new FormData();
      fd.append("audio_blob", this.store_audio_blob);
      fd.append("age", this.store_model.age);
      fd.append("gender", this.store_model.gender);
      fd.append("profession", this.store_model.profession);
      fd.append("birth_city", this.store_model.birth_city);
      fd.append("current_city", this.store_model.current_city);
      fd.append(
        "years_on_current_city",
        this.store_model.years_on_current_city
      );
      fd.append(
        "parents_original_city",
        this.store_model.parents_original_city
      );
      fd.append("recaptcha_token", recaptchaToken);
      // TODO: Get sentence from page
      fd.append("sentence", "A Amazônia é a reserva ecológica do globo");
      fetch(config.api.createRecordUrl, {
        headers: { Accept: "application/json" },
        method: "POST",
        body: fd,
      })
        .then((response) => {
          if (response.status === 200) {
            this.$store.dispatch("form/setAudioBlob", null);
            alert("Áudio publicado com sucesso!");
          } else {
            alert("Erro ao publicar áudio!");
          }
        })
        .catch((err) => {
          //helper to get a displayable message to the user
          function getErrorMessage(err) {
            let responseBody;
            responseBody = err.response;
            if (!responseBody) {
              responseBody = err;
            } else {
              responseBody = err.response.data || responseBody;
            }
            return responseBody.message || JSON.stringify(responseBody);
          }
          this.serverError = getErrorMessage(err);
        });

      // this.axios
      //   .post(config.api.createRecordUrl, {
      //     form_data: this.store_model,
      //     audio_blob: this.store_audio_blob,
      //     recaptchaToken: recaptchaToken,
      //   })
      //   .then((response) => {
      //     this.sucessfulServerResponse = response.data.message;
      //   })
      //   .catch((err) => {
      //     this.serverError = getErrorMessage(err);
      //     //helper to get a displayable message to the user
      //     function getErrorMessage(err) {
      //       let responseBody;
      //       responseBody = err.response;
      //       if (!responseBody) {
      //         responseBody = err;
      //       } else {
      //         responseBody = err.response.data || responseBody;
      //       }
      //       return responseBody.message || JSON.stringify(responseBody);
      //     }
      //   });
    },
    onCaptchaExpired: function () {
      this.$refs.recaptcha.reset();
    },
    validateIntroductionTab() {
      const ok = this.$refs.introductionTab.validate();
      if (ok) {
        this.$store.dispatch("form/setModel", this.model);
      }
      return ok;
    },
    validatePersonalInformationTab() {
      const ok = this.$refs.personalInformationTab.validate();
      if (ok) {
        this.$store.dispatch("form/setModel", this.model);
      }
      return ok;
    },
  },
};
</script>

<style>
#eu-li-e-aceito-as-condies-descritas-acima {
  position: absolute;
  vertical-align: middle;
  left: 49vw;
}
</style>