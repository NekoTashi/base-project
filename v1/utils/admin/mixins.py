class ShowFieldsAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ShowFieldsAdminMixin, self).__init__(model, admin_site)
