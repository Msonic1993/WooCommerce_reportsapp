var formatBackground=function(){
	var table, tbody, rowCount, cellCount, value;
	table=document.getElementsByTagName('table')[0];
	if(table.childNodes[1]) tbody=table.childNodes[1];
	if(tbody) rowCount=tbody.childNodes.length;

	for(i=0;i<rowCount;i++){
		cellCount=tbody.childNodes[i].childNodes.length;

		for(j=1;j<cellCount;j++){
			value=tbody.childNodes[i].childNodes[j].outerText;
			if(parseInt(value)<0) tbody.childNodes[i].childNodes[j].setAttribute('style','color: #f00');
			j+=1;
		}
		i+=1;
	}
};

formatBackground();