from clipper_admin import ClipperConnection, DockerContainerManager
clipper_conn = ClipperConnection(DockerContainerManager())
clipper_conn.connect()

import sys
sys.path.append('./')
print(sys.path)

from predict_example import python

from clipper_admin.deployers import python as python_deployer

python_deployer.deploy_python_closure(clipper_conn, name="sum-model", version=1, input_type="doubles", func=python.predict)

