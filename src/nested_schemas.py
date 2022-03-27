from typing import Optional

import pydantic
import graphene
from graphene_pydantic import PydanticObjectType, PydanticInputObjectType


class TagModel(pydantic.BaseModel):
    object_id: str
    category: 'CategoryModel'
    title: str


class CategoryModel(pydantic.BaseModel):
    object_id: str
    title: str
    description: Optional[str]
    tags: Optional[list[TagModel]]


TagModel.update_forward_refs()


class PaginateCategoryModel(pydantic.BaseModel):
    items: list[CategoryModel]
    key: str


class PaginateTagModel(pydantic.BaseModel):
    items: list[TagModel]
    key: str


class Tag(PydanticObjectType):
    class Meta:
        model = TagModel


class Category(PydanticObjectType):
    class Meta:
        model = CategoryModel


class PaginateCategory(PydanticObjectType):
    class Meta:
        model = PaginateCategoryModel


class PaginateTag(PydanticObjectType):
    class Meta:
        model = PaginateTagModel


category1 = CategoryModel(object_id="1", title="fasfafasf")
category2 = CategoryModel(object_id="2", title="bxcbxcb")
category3 = CategoryModel(object_id="3", title="utyutu")

tag1 = TagModel(object_id="1", category=category1, title="sport")
tag2 = TagModel(object_id="2", category=category2, title="love")
tag3 = TagModel(object_id="3", category=category1, title="football")
tag4 = TagModel(object_id="4", category=category1, title="hockey")

category1.tags = [tag1, tag3, tag4]
category2.tags = [tag2]

categories_data = {
    "items": [category1, category2, category3],
    "key": "fagag"
}
tags_data = {
    "items": [tag1, tag2, tag3],
    "key": "fagag"
}

paginate_categories_data = PaginateCategoryModel(**categories_data)
paginate_tags_data = PaginateTagModel(**tags_data)


class CategoryQuery(graphene.ObjectType):
    nested_list_categories = graphene.Field(PaginateCategory)
    nested_list_tags = graphene.Field(PaginateTag)

    def resolve_nested_list_categories(self, info):
        return paginate_categories_data

    def resolve_nested_list_tags(self, info):
        return paginate_tags_data


class CategoryInput1(PydanticInputObjectType):
    class Meta:
        model = CategoryModel
        exclude_fields = ("tags",)


class TagInput(PydanticInputObjectType):
    class Meta:
        model = TagModel
        exclude_fields = ("category",)

    category = graphene.InputField(CategoryInput1)


class CategoryInput(PydanticInputObjectType):
    class Meta:
        model = CategoryModel
        exclude_fields = ("tags",)

    tags = graphene.InputField(graphene.List(TagInput))


class CategoryOutput(PydanticObjectType):
    class Meta:
        model = CategoryModel


class CreateCategory(graphene.Mutation):
    class Arguments:
        category = CategoryInput()

    Output = CategoryOutput

    @staticmethod
    def mutate(parent, info, category):
        # TODO: save to db
        return category


class BulkCreateCategory(graphene.Mutation):
    class Arguments:
        categories = graphene.List(CategoryInput)

    Output = graphene.List(CategoryOutput)

    @staticmethod
    def mutate(parent, info, categories):
        # TODO: save to db
        return categories


class UpdateCategory(graphene.Mutation):
    class Arguments:
        category = CategoryInput()

    Output = CategoryOutput

    @staticmethod
    def mutate(parent, info, category):
        # TODO: save to db
        return category


class BulkUpdateCategory(graphene.Mutation):
    class Arguments:
        categories = graphene.List(CategoryInput)

    Output = graphene.List(CategoryOutput)

    @staticmethod
    def mutate(parent, info, categories):
        # TODO: save to db
        return categories


class TagOutput(PydanticObjectType):
    class Meta:
        model = TagModel


class CreateTag(graphene.Mutation):
    class Arguments:
        tag = TagInput()

    Output = TagOutput

    @staticmethod
    def mutate(parent, info, tag):
        # TODO: save to db
        return tag


class BulkCreateTag(graphene.Mutation):
    class Arguments:
        tags = graphene.List(TagInput)

    Output = graphene.List(TagOutput)

    @staticmethod
    def mutate(parent, info, tags):
        # TODO: save to db
        return tags


class UpdateTag(graphene.Mutation):
    class Arguments:
        tag = TagInput()

    Output = TagOutput

    @staticmethod
    def mutate(parent, info, tag):
        # TODO: save to db
        return tag


class BulkUpdateTag(graphene.Mutation):
    class Arguments:
        tags = graphene.List(TagInput)

    Output = graphene.List(TagOutput)

    @staticmethod
    def mutate(parent, info, tags):
        # TODO: save to db
        return tags


class CategoryMutation(graphene.ObjectType):
    create_category_nested = CreateCategory.Field()
    update_category_nested = UpdateCategory.Field()
    create_tag_nested = CreateTag.Field()
    update_tag_nested = UpdateTag.Field()
    bulk_create_tag_nested = BulkCreateTag.Field()
    bulk_update_tag_nested = BulkUpdateTag.Field()
    bulk_create_category_nested = BulkCreateCategory.Field()
    bulk_update_category_nested = BulkUpdateCategory.Field()


Tag.resolve_placeholders()
Category.resolve_placeholders()

category_schema = graphene.Schema(query=CategoryQuery, mutation=CategoryMutation)
