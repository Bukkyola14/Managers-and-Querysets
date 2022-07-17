class LinkSerializer(serializers.ModelSerializer):

    class Meta:
	model = Link
	fields = “__all__”