import config from "../../config";
import axios from 'axios'

// initial state
const state = () => ({
    model: null,
    audioBlob: null,
    genderList: [],
    birthCityList: [],
    currentCityList: [],
    parentsCityList: [],
    stateList: [],
    sentence: "",
    recordState: "",
});

// getters
const getters = {
    model: state => state.model,
    audioBlob: state => state.audioBlob,
    genderList: state => state.genderList,
    birthCityList: state => state.birthCityList,
    currentCityList: state => state.currentCityList,
    parentsCityList: state => state.parentsCityList,
    stateList: state => state.stateList,
    sentence: state => state.sentence,
    recordState: state => state.recordState,
};

// actions
const actions = {
    setModel: ({ commit }, model) => commit('setModel', model),
    setAudioBlob: ({ commit }, audioBlob) => commit('setAudioBlob', audioBlob),
    fetchGenderList: ({ commit }) => {
        let genders = config.genders;
        commit('setGenderList', genders);
    },
    fetchBirthCityList: ({ commit }, state) => {
        let cities = config.cities[state];
        commit('setBirthCityList', cities);
    },
    fetchCurrentCityList: ({ commit }, state) => {
        let cities = config.cities[state];
        commit('setCurrentCityList', cities);
    },
    fetchParentsCityList: ({ commit }, state) => {
        let cities = config.cities[state];
        commit('setParentsCityList', cities);
    },
    fetchStateList: ({ commit }) => {
        let states = Object.keys(config.cities);
        states.sort();
        commit('setStateList', states);
    },
    fetchSentence: ({ commit }, state) => {
        function getSentence(url) {
            axios
                .get(url)
                .then(({ data }) => {
                    commit('setSentence', data.results[0].text)
                })
        }
        let url = config.api.getSentenceUrl + "?state=" + state
        getSentence(url)
    },
    fetchRecordState: ({ commit }) => {
        navigator.permissions
            .query({ name: "microphone" })
            .then(function(permissionStatus) {
                commit('setRecordState', permissionStatus.state);
                console.log(permissionStatus.state); // granted, denied, prompt
                permissionStatus.onchange = function() {
                    commit('setRecordState', permissionStatus.state);
                    console.log("Permission changed to " + this.state);
                };
            });
    },
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
    setBirthCityList: (state, birthCityList) => {
        state.birthCityList = birthCityList;
    },
    setCurrentCityList: (state, currentCityList) => {
        state.currentCityList = currentCityList;
    },
    setParentsCityList: (state, parentsCityList) => {
        state.parentsCityList = parentsCityList;
    },
    setStateList: (state, stateList) => {
        state.stateList = stateList;
    },
    setSentence: (state, sentence) => {
        state.sentence = sentence;
    },
    setRecordState: (state, recordState) => {
        state.recordState = recordState;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};