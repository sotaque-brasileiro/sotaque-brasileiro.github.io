// initial state
const state = () => ({
  model: null,
  audioBlob: null,
});

// getters
const getters = {
  model: state => state.model,
  audioBlob: state => state.audioBlob,
};

// actions
const actions = {
  setModel: ({ commit }, model) => commit('setModel', model),
  setAudioBlob: ({ commit }, audioBlob) => commit('setAudioBlob', audioBlob)
};

// mutations
const mutations = {
  setModel: (state, model) => {
    state.model = model;
  },
  setAudioBlob: (state, audioBlob) => {
    state.audioBlob = audioBlob;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};