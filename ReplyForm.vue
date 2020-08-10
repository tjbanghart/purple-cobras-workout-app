<template>
  <div class="reply-form">
    <base-textarea
      v-model="content"
      ref="input"
      placeholder="Your reply goes here..."
      :min-height="150"
      :disabled="loading"
    />
    <div class="replyFormButtonBar">


    <base-button
      class="insertPictureButton"
      :disabled="loading"
      @click="reply"
    >
      {{ loading ? 'Loading...' : 'Insert Picture' }}
    </base-button>


    <base-button
      class="insertVideoButton"
      :disabled="loading"
      @click="reply"
    >
      {{ loading ? 'Loading...' : 'Insert Video' }}
    </base-button>


    <base-button
      class="reply-button"
      :disabled="loading"
      @click="reply"
    >
      {{ loading ? 'Replying...' : 'Reply' }}
    </base-button>

    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { required } from 'vuelidate/lib/validators'

export default {
  data () {
    return {
      content: '',
      loading: false
    }
  },

  validations: {
    content: { required }
  },

  methods: {
    ...mapActions(['addReply']),
    async reply () {
      this.$v.$touch()
      if (!this.$v.$anyError) {
        this.loading = true
        try {
          await this.addReply({ data: { content: this.content } })
          this.content = ''
          this.$v.$reset()
          this.loading = false
        } catch (err) {
          this.loading = false
        }
      }
    },

    focus () {
      this.$refs.input.focus()
    }
  }
}
</script>

<style lang="stylus" scoped>
.reply-form
  display: flex
  justify-content: center
  flex-direction: column
  margin: 30px auto
  width: 80%

.reply-button
  margin-left: 10px
  margin-right: 10px

.insertPictureButton
  margin-left: 10px
  margin-right: 10px


.insertVideoButton
  margin-left: 10px
  margin-right: 10px

.replyFormButtonBar
  align-self: flex-end
  margin-top: 5px

</style>
