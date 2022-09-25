from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    """Test Serializer"""

    name = serializers.CharField(max_length=10)


"""
Serializer fields
	Core arguments

Boolean fields
	BooleanField

String fields
	CharField
	EmailField
	RegexField
	SlugField
	URLField
	UUIDField
	FilePathField
	IPAddressField

Numeric fields
	IntegerField
	FloatField
	DecimalField

Date and time fields
	DateTimeField
	DateField
	TimeField
	DurationField

Choice selection fields
	ChoiceField
	MultipleChoiceField

File upload fields
	Parsers and file uploads.
	FileField
	ImageField

Composite fields
	ListField
	DictField
	HStoreField
	JSONField

Miscellaneous fields
	ReadOnlyField
	HiddenField
	ModelField
	SerializerMethodField

Custom fields
	Examples

Third party packages
	DRF Compound Fields
	DRF Extra Fields
"""
