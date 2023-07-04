
class BaseService:


    def get_update_queryset(self, view, params={}):
        return view.queryset.filter(**params).order_by("-created_at")
    

    def create(self, data, view):
        upload_images = data.get("upload_images")
        if upload_images:
          image_queryset = view.image_queryset
          del data["upload_images"]
        obj = view.queryset.create(**data)
        if upload_images:
            for image in upload_images:
                image_queryset.create(resume=obj, image=image)
        return obj

                
                
    