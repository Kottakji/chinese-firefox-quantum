chrome.browserAction.onClicked.addListener(ppcMain.inlineToggle);
chrome.tabs.onActivated.addListener(ppcMain.onTabSelect);
chrome.runtime.onMessage.addListener(
	function(request, sender, response) {
		switch(request.type) {
			case 'enable?':
				console.log('enable?');
				ppcMain.onTabSelect(sender.tab.id);
				response(ppcMain.config.toggleKey);
				break;
			case 'enable-via-hotkey':
				ppcMain.inlineToggle();
				ppcMain.onTabSelect(sender.tab.id);
				break;
			case 'xsearch':
				var e = ppcMain.search(request.text, request.showmode);
				response(e);
				break;
			//case 'translate':  # What is the use of this function?
			//	var e = ppcMain.dict.translate(request.title);
			//	response(e);
			//	break;
			case 'makehtml':
				var html = ppcMain.dict.makeHtml(request.entry);
				response(html);
				break;
			case 'reloadxsearch':
				// If the user changes from mandarin to cantonese, we need to reload the dictionary
				ppcMain.loadDictionary();
				var e = ppcMain.search(request.text, request.showmode);
				response(e);
				break;
			default:
				console.log(request);
		}
	});
	
if(initStorage("v0.9", true)) {
	// v0.7
	initStorage("popupcolor", "charcoal");
	initStorage("highlight", "yes");
	initStorage("docolors", "yes");
	initStorage("showhanzi", "boths");
	initStorage("pinyin", "tonemarks");
	initStorage("dialect", "mandarin");
	initStorage("toggleKey", "Shift+P");

	// v0.8
	// No changes to options
}

/** 
* Initializes the localStorage for the given key. 
* If the given key is already initialized, nothing happens. 
* 
* @author Teo (GD API Guru)
* @param key The key for which to initialize 
* @param initialValue Initial value of localStorage on the given key 
* @return true if a value is assigned or false if nothing happens 
*/ 
function initStorage(key, initialValue) { 
  var currentValue = localStorage[key]; 
  if (!currentValue) { 
	localStorage[key] = initialValue; 
	return true; 
  } 
  return false; 
} 

ppcMain.config = {};
ppcMain.config.css = localStorage["popupcolor"];
ppcMain.config.highlight = localStorage["highlight"];
ppcMain.config.showhanzi = localStorage["showhanzi"];
ppcMain.config.docolors = localStorage["docolors"];
ppcMain.config.pinyin = localStorage["pinyin"];
ppcMain.config.dialect = localStorage["dialect"];
ppcMain.config.toggleKey = localStorage["toggleKey"];