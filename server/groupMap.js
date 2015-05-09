function groupMap(){
	//find words in the document text
/*	var words = this.Group.match(/\w+/g);
	
	if (words == null){
		return;
	
	}


	for (var i = 0; i < words.length; i++){
		//emit every word, with count of one
		emit(words[i], {count: 1});
	}*/
	emit(
		{group_id: this.group_id, queries:this.cQueries}, {exists: 1}
	);
}
