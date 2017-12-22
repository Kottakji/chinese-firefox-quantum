function onLoaded() {
    function fillVals() {
        var store = localStorage['popupcolor'];
        for (var i = 0; i < document.optform.popupcolor.length; ++i) {
            if (document.optform.popupcolor[i].value == store) {
                document.optform.popupcolor[i].selected = true;
                break;
            }
        }

        store = localStorage['highlight'];
        if (store == 'yes') {
            document.optform.highlighttext[0].selected = true;
        }
        else
            document.optform.highlighttext[1].selected = true;

        store = localStorage['pinyin'];
        for (var i = 0; i < document.optform.pinyin.length; ++i) {
            if (document.optform.pinyin[i].value == store) {
                document.optform.pinyin[i].selected = true;
                break;
            }
        }

        store = localStorage['showhanzi'];
        for (var i = 0; i < document.optform.showhanzi.length; ++i) {
            if (document.optform.showhanzi[i].value == store) {
                document.optform.showhanzi[i].selected = true;
                break;
            }
        }

        store = localStorage['dialect'];
        for (var i = 0; i < document.optform.dialect.length; ++i) {
            if (document.optform.dialect[i].value == store) {
                document.optform.dialect[i].selected = true;
                break;
            }
        }

        store = localStorage['docolors'];
        if (store == 'yes') {
            document.optform.docolors[0].selected = true;
        }
        else
            document.optform.docolors[1].selected = true;
    }

    function getVals() {
        localStorage['popupcolor'] = document.optform.popupcolor.value;
        localStorage['highlight'] = document.optform.highlighttext.value;
        localStorage['pinyin'] = document.optform.pinyin.value;
        localStorage['docolors'] = document.optform.docolors.value;
        localStorage['showhanzi'] = document.optform.showhanzi.value;
        localStorage['dialect'] = document.optform.dialect.value;

        chrome.extension.getBackgroundPage().ppcMain.config.css = localStorage["popupcolor"];
        chrome.extension.getBackgroundPage().ppcMain.config.highlight = localStorage["highlight"];
        chrome.extension.getBackgroundPage().ppcMain.config.pinyin = localStorage["pinyin"];
        chrome.extension.getBackgroundPage().ppcMain.config.docolors = localStorage["docolors"];
        chrome.extension.getBackgroundPage().ppcMain.config.showhanzi = localStorage["showhanzi"];
        chrome.extension.getBackgroundPage().ppcMain.config.dialect = localStorage["dialect"];
    }

    document.getElementById('optform').onsubmit = function (e) {
        e.preventDefault();
        getVals();

        // Reload the dictionary
        chrome.extension.getBackgroundPage().ppcMain.dict = false;
        chrome.extension.getBackgroundPage().ppcMain.loadDictionary();
    };

    fillVals();


    // Mandarin or Cantonese
    var dialect = document.getElementById('dialect');
    dialect.addEventListener('change', function (e) {
        displayShowHanzi(e.target.value)
    });

    displayShowHanzi(dialect.options[dialect.selectedIndex].value);

    function displayShowHanzi (value) {
        if (value === 'cantonese') {
            document.getElementById('showhanzi-div').style.display = 'none';
        } else {
            document.getElementById('showhanzi-div').style.display = 'block';
        }
    }

}

if (window.addEventListener) {
    window.addEventListener('load', onLoaded, false);
} else {
    window.attachEvent('onload', onLoaded);
}
