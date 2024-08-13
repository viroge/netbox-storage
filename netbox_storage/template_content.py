#from extras.plugins import PluginTemplateExtension
from netbox.plugins import PluginTemplateExtension
from .models import VMDK


class VMVMDKCard(PluginTemplateExtension):
    model = 'virtualization.virtualmachine'

    def left_page(self):
        return self.render('netbox_storage/vm_vmdk_extend.html',
                           extra_context={'object': self.context['object']})


template_extensions = [VMVMDKCard]
