
//lists the posts that are under each category
//ie If a user selected Arms the categoryTitle would be arms.  Therefore,
//they would see two threads they could read or comment on
export default (categorySlug) => {
  const categoryTitle = categorySlug

//allows us to select an individual thread and view the comments
//URL follows a pattern of c#t#.  C is for the category #.  ie Arms is C1, Abs is C2, etc
//T is for thread.  ie under Arms we have 5 threads.  Therefore we would have c1t1, c1t2, c1t3, c1t4, c1t5
  function getTopicId (id) {
    switch (categorySlug) {
      case 'Arms':
       	 return `c1t${id}`
      case 'Abs':
       	 return `c2t${id}`
		 case 'Shoulders':
       	 return `c3t${id}`
		 case 'Chest':
       	 return `c4t${id}`
		 case 'Core':
       	 return `c5t${id}`
		 case 'Back':
       	 return `c6t${id}`
      default:
        return `c7t${id}`
    }
  }
if (categoryTitle === 'Arms') {
  return [
    {
      _id: getTopicId(1),
      title: `Arms - Curls for the Girls`,
      user: { name: 'Dave'},
      views: 'Read',
      numberOfReplies: 2,
      category: { slug: categorySlug },
      createdAt: (new Date()).setDate(new Date().getDate() - 2)
    },
    {
      _id: getTopicId(2),
      title: `${categoryTitle} have never been bigger`,
      user: { name: 'Paul'},
      views: 'Unread',
      numberOfReplies: 0,
      category: { slug: categorySlug },
      createdAt: (new Date()).setDate(new Date().getDate() - 1)
    }
  ]
}
else if (categoryTitle === 'Abs'){
return [
    {
      _id: getTopicId(3),
      title: `Six Pack`,
      user: { name: 'Dave', avatar: '' },
      views: 'Read',
      numberOfReplies: 2,
      category: { slug: categorySlug },
      createdAt: (new Date()).setDate(new Date().getDate() - 2)
    }
  ]

}
else if (categoryTitle === 'Shoulders'){
return [
    {
      _id: getTopicId(6),
      title: `Why Shoulders are so important`,
      user: { name: 'Dave'},
      views: 'Unread',
      numberOfReplies: 2,
      category: { slug: categorySlug },
      createdAt: (new Date()).setDate(new Date().getDate() - 2)
    }
  ]

}
else if (categoryTitle === 'Chest'){
return [
  ]

}
else if (categoryTitle === 'Core'){
return [
  ]

}
else if (categoryTitle === 'Back'){
return [
  ]

}
else if (categoryTitle === 'Legs'){
return [
  ]

}
else if (categoryTitle === 'Unread'){
return [
{
      _id: getTopicId(2),
      title: `${categoryTitle} have never been bigger`,
      user: { name: 'Paul'},
      views: 'Unread',
      numberOfReplies: 0,
      category: { slug: categorySlug },
      createdAt: (new Date()).setDate(new Date().getDate() - 1)
    },
	{
      _id: getTopicId(6),
      title: `Why Shoulders are so important`,
      user: { name: 'Dave'},
      views: 'Unread',
      numberOfReplies: 2,
      category: { slug: categorySlug },
      createdAt: (new Date()).setDate(new Date().getDate() - 2)
    }
	
  ]

}
else if (categoryTitle === 'Read'){
return [
 {
      _id: getTopicId(1),
      title: `Arms - Curls for the Girls`,
      user: { name: 'Dave'},
      views: 'Read',
      numberOfReplies: 2,
      category: { slug: categorySlug },
      createdAt: (new Date()).setDate(new Date().getDate() - 2)
    },
	{
      _id: getTopicId(3),
      title: `Six Pack`,
      user: { name: 'Dave', avatar: '' },
      views: 'Read',
      numberOfReplies: 2,
      category: { slug: categorySlug },
      createdAt: (new Date()).setDate(new Date().getDate() - 2)
    }
  ]

}
//wanted to set it to something so I knew the code wasn't working.  We should never get here
else {
return [
{
      _id: getTopicId(1),
      title: `Testing`,
      user: { name: 'Dave'},
      views: 'Read',
      numberOfReplies: 2,
      category: { slug: categorySlug },
      createdAt: (new Date()).setDate(new Date().getDate() - 2)
    }
  ]

}
}
