import config from "../../config";
import axios from 'axios'

// initial state
const state = () => ({
  model: null,
  audioBlob: null,
  genderList: [],
  cityList: [],
  stateList: [],
});

// getters
const getters = {
  model: state => state.model,
  audioBlob: state => state.audioBlob,
  genderList: state => state.genderList,
  cityList: state => state.cityList,
  stateList: state => state.stateList,
};

// actions
const actions = {
  setModel: ({ commit }, model) => commit('setModel', model),
  setAudioBlob: ({ commit }, audioBlob) => commit('setAudioBlob', audioBlob),
  fetchGenderList: ({ commit }) => {
    function getGenders(url) {
      axios
        .get(url)
        .then(({ data }) => {
          data.results.forEach((item) => {
            genders.push(item.radio_text)
          })
          if (data.next) {
            getGenders(data.next)
          }
        })
    }
    let genders = []
    let url = config.api.getGendersUrl
    getGenders(url)
    commit('setGenderList', genders)
  },
  // TODO: Filter cities by state, when selected
  fetchCityList: ({ commit }) => {
    function mergeCityName(item) {
      return item.name + "/" + item.state.abbreviation;
    }
    function getCities(url) {
      axios
        .get(url)
        .then(({ data }) => {
          data.results.forEach((item) => {
            cities.push(mergeCityName(item))
          })
          if (data.next) {
            getCities(data.next)
          }
        })
    }
    let cities = []
    let url = config.api.getCitiesUrl
    getCities(url)
    commit('setCityList', cities)
  },
  // TODO: Review this piece of code
  fetchStateList: ({ commit }) => {
    function getStates(url) {
      axios
        .get(url)
        .then(({ data }) => {
          data.results.forEach((item) => {
            states.push(item.name)
          })
          if (data.next) {
            getStates(data.next)
          }
        })
    }
    let states = []
    let url = config.api.getStatesUrl
    getStates(url)
    commit('setStateList', states)
  }
};

// mutations
const mutations = {
  setModel: (state, model) => {
    state.model = model;
  },
  setAudioBlob: (state, audioBlob) => {
    state.audioBlob = audioBlob;
  },
  setGenderList: (state, genderList) => {
    state.genderList = genderList;
  },
  setCityList: (state, cityList) => {
    state.cityList = cityList;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};