from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language',
                  'style']

    def create(self, validated_data):
        """
        Create and return a new 'Snippet' instance, given validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Snippet' instance, given validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.owner = serializers.ReadOnlyField(source='owner.username')
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail',
                                                   read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
