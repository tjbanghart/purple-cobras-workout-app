//import categories from './data/categories'
import topicsInCategory from './data/topicsInCategory'
import topic from './data/topic'
import userData from './data/userData'

//https://www.w3schools.com/nodejs/nodejs_mongodb_query.asp
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("purpleCobraForum");
  var categories = dbo.collection("category").find({}).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});


const fetch = (mockData, time = 100) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(mockData)
    }, time)
  })
}

export default {
  getCategories () {
    return fetch(categories)
  },

  getCategory (categorySlug) {
    const category = categories
    if (!category) {
      throw Error('Category not found')
    }
    return fetch(category)
  },

  createCategory (data) {
    return fetch({ slug: 'mocked-category' })
  },

  updateCategory (categorySlug, data) {
    return fetch(categorySlug)
  },

  deleteCategory (categorySlug) {
    return fetch(true)
  },

  getTopics (filters) {
    if (filters.categorySlug) {
      return fetch(topicsInCategory(filters.categorySlug))
    }
  },

  getTopic (topicId) {
    const fetchedTopic = topic(topicId)
    if (!fetchedTopic) {
      throw Error('Topic not found')
    }
    return fetch(fetchedTopic)
  },

  createTopic (data) {
    return fetch({ _id: 1 })
  },

  updateTopic (topicId, data) {
    return fetch(topicId)
  },

  deleteTopic (topicId) {
    return fetch(true)
  },

  addReply (topicId, data) {
    const user = JSON.parse(localStorage.getItem('mocked_user'))
    return fetch({
      _id: Math.round(Math.random() * 99999),
      content: data.content,
      createdAt: new Date(),
      user
    })
  },

  deleteReply (topicId, replyId) {
    return fetch(true)
  },

  updateReply (topicId, replyId, data) {
    return fetch(data)
  },

  registerUser (data) {},

  login ({ email, password }) {
    const user = userData(email)
    localStorage.setItem('mocked_user', JSON.stringify(user))
    return fetch({
      user,
      token: 'mockedtoken'
    })
  },

  getUserData () {
    return fetch(JSON.parse(localStorage.getItem('mocked_user')))
  },

  updateUserProfile ({ data }) {},

  updateUserPassword ({ data }) {}
}
