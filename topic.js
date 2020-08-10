//Here we list the individual posts and their replies

export default (topicId) => {
	//limited what was returned so I removed it.
 // if (!(/c[1-20]t[1-20]/).test(topicId)) {
//    return null
 // }
  function getCategorySlug () {
    if (topicId.indexOf('c1') === 0) {
      return 'Arms'
    } else if (topicId.indexOf('c2') === 0) {
      return 'Abs'
    }else if (topicId.indexOf('c3') === 0) {
      return 'Shoulders'
    }
	else if (topicId.indexOf('c4') === 0) {
      return 'Chest'
    }
	else if (topicId.indexOf('c5') === 0) {
      return 'Core'
    }
	else if (topicId.indexOf('c6') === 0) {
      return 'Back'
    }else {
      return 'Legs'
    }
  }

if(topicId.indexOf('t1') === 2) {
  return {
    _id: 1,
    title: 'Curls for the girls',
    user: {
      name: 'Dave'
    },
    content: 'I can not believe people think that was hard',
    category: {  _id: 1,
    user: {
      name: 'Dave'
    },
    replies: [
    ] },
    createdAt: '2020-08-01',
    replies: [
      {
        _id: 1,
        user: {
          name: 'Judy'
        },
        content: 'Dave taking steroids?',
        createdAt: '2020-08-02'
      }
    ]
  }

}
else if(topicId.indexOf('t2') === 2) {
  return {
     _id: 2,
    title: 'Arms have never been bigger',
    user: {
      name: 'Dave'
    },
    content: 'You wish your arms were as big as mine',
    category: {  _id: 2,
    user: {
      name: 'Dave'
    },
    replies: [
    ] },
    createdAt: '2020-08-01',
    replies: [
      
    ]
  }
}
else if(topicId.indexOf('t3') === 2) {
  return {
    _id: 1,
    title: 'I have a six pack',
    user: {
      name: 'Dave'
    },
    content: 'You all are fat, I have a six pack',
    category: {  _id: 1,
    user: {
      name: 'Dave'
    },
    replies: [
    ] },
    createdAt: '2020-08-01',
    replies: [
      {
        _id: 1,
        user: {
          name: 'Paul'
        },
        content: 'You must be busy with all the girls who chase you, wait you are a loser who has time to post',
        createdAt: '2020-08-02'
      }
    ]
  }
}
else if(topicId.indexOf('t4') === 2) {
  return {
      }
}
else if(topicId.indexOf('t5') === 2) {
  return {
  
  }
}
else if(topicId.indexOf('t6') === 2) {
  return {
    _id: 1,
    title: 'Why Shoulders are so important',
    user: {
      name: 'Dave',
      avatar: ''
    },
    content: 'My bench increased 20% after working out my shoulders',
    category: {  _id: 1,
    title: 'One - I had no problems with the workout',
    user: {
      name: 'Dave',
      avatar: ''
    },
    content: '',
    category: { slug: getCategorySlug() },
    createdAt: '2020-08-01',
    replies: [
    ] },
    createdAt: '2020-08-01',
    replies: [
      {
        _id: 1,
        user: {
          name: 'Judy',
          avatar: ''
        },
        content: 'Mine increased 25%, they are really important',
        createdAt: '2020-08-02'
      },
	   {
        _id: 1,
        user: {
          name: 'Larry',
          avatar: ''
        },
        content: 'Nobody cares about shoulders',
        createdAt: '2020-08-02'
      }
    ]
  }
}
else if(topicId.indexOf('t7') === 2) {
  return {
  }
}
//we should never get here
else {
	return {
  }
	
	
}
}
