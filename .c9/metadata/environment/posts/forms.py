{"filter":false,"title":"forms.py","tooltip":"/posts/forms.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":6,"column":71},"action":"remove","lines":["from django import forms","from .models import Post","","class BlogPostForm(forms.ModelForm):","    class Meta:","        model = Post","        fields = ('title', 'content', 'image', 'tag', 'published_date')"],"id":1},{"start":{"row":0,"column":0},"end":{"row":8,"column":71},"action":"insert","lines":["from django import forms","from .models import Post","","","class BlogPostForm(forms.ModelForm):","","    class Meta:","        model = Post","        fields = ('title', 'content', 'image', 'tag', 'published_date')"]}]]},"ace":{"folds":[],"customSyntax":"xquery","scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":71},"end":{"row":8,"column":71},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1583259277101,"hash":"89111f5fb87802977bfff76ecc6483d0da3a3d8e"}