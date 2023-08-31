<template>
  <div class="music-player">
    <div class="stream-input">
      <input v-model="inputStreamURL" placeholder="Enter stream URL" />
      <button @click="loadStream">Load Stream</button>
    </div>

    <audio ref="audioElement" :src="streamURL"></audio>

    <div class="controls">
      <button @click="togglePlay">{{ isPlaying ? 'Pause' : 'Play' }}</button>
      <button @click="stop">Stop</button>
      <button @click="muteToggle">{{ isMuted ? 'Unmute' : 'Mute' }}</button>
    </div>

    <div class="progress-bar-container">
      <span>{{ formatTime(currentTime) }}</span>
      <div class="progress-bar" @click="seek($event)">
        <div class="filler" :style="{ width: progress + '%' }"></div>
      </div>
      <span>{{ formatTime(duration - currentTime) }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputStreamURL: '',
      streamURL: '',
      isPlaying: false,
      isMuted: false,
      currentTime: 0,
      duration: 0,
    }
  },
  computed: {
    progress() {
      return (this.currentTime / this.duration) * 100;
    }
  },
  methods: {
    loadStream() {
      this.streamURL = this.inputStreamURL;
      this.stop(); // Stop and reset the player
    },
    togglePlay() {
      const audio = this.$refs.audioElement;
      if (audio.paused) {
        audio.play();
        this.isPlaying = true;
      } else {
        audio.pause();
        this.isPlaying = false;
      }
    },
    stop() {
      const audio = this.$refs.audioElement;
      audio.pause();
      audio.currentTime = 0;
      this.isPlaying = false;
    },
    muteToggle() {
      const audio = this.$refs.audioElement;
      audio.muted = !audio.muted;
      this.isMuted = audio.muted;
    },
    updateAudioData(event) {
      this.currentTime = event.target.currentTime;
      if (!this.duration) { // set duration only once
        this.duration = event.target.duration;
      }
    },
    loadMetaData(event) {
      this.duration = event.target.duration;
    },
    formatTime(seconds) {
      const mins = Math.floor(seconds / 60);
      const secs = Math.floor(seconds % 60);
      return `${mins}:${secs.toString().padStart(2, '0')}`;
    },
    seek(event) {
      const bar = this.$el.querySelector('.progress-bar');
      const clickPosition = (event.pageX - bar.offsetLeft) / bar.offsetWidth;
      const audio = this.$refs.audioElement;
      audio.currentTime = clickPosition * audio.duration;
    },
    formatTime(seconds) {
      const mins = Math.floor(seconds / 60);
      const secs = Math.floor(seconds % 60);
      return `${mins}:${secs.toString().padStart(2, '0')}`;
    },
    mounted() {
      const audio = this.$refs.audioElement;
      audio.addEventListener('timeupdate', this.updateAudioData);
      audio.addEventListener('loadedmetadata', this.loadMetaData);
    },
    beforeDestroy() {
      const audio = this.$refs.audioElement;
      audio.removeEventListener('timeupdate', this.updateAudioData);
      audio.addEventListener('loadedmetadata', this.loadMetaData);
    }
  }
}
</script>

<style>
.music-player .stream-input {
  margin-bottom: 10px;
}

.music-player button {
  margin-right: 10px;
}

.progress-bar-container {
  display: flex;
  align-items: center;
}

.progress-bar {
  flex-grow: 1;
  margin: 0 10px;
  height: 20px;
  background-color: #e0e0e0;
  position: relative;
  cursor: pointer;
}

.filler {
  height: 100%;
  background-color: #2196F3;
  /* indigo color for the filled part */
  width: 0;
  /* Initial width; will be set by Vue dynamically */
}
</style>
