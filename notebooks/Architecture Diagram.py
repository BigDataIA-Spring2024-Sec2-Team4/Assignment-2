from diagrams import Diagram, Node, Cluster, Edge
from diagrams.custom import Custom
from diagrams.generic.database import SQL
from diagrams.aws.storage import S3
from diagrams.onprem.database import Mysql
from diagrams.onprem.database import Mongodb
from diagrams.onprem.database import Oracle
from urllib.request import urlretrieve
from diagrams.onprem.workflow import Nifi
from diagrams.generic.storage import Storage
from diagrams.aws.storage import SimpleStorageServiceS3Bucket



# Import custom icons for XML, PDF, spider middleware, spider, GROBID, Playwright, and scheduler
with Diagram("Assignment 2 diagram", show=False, direction="LR", outformat="png") as print:

 # Create nodes for AWS services
  sql_node = Node("SQL")  # Use only the node name without associating a class
  # s3_bucket_node = Node("S3 Bucket", SimpleStorageServiceS3Bucket)


  # Create a XML icon
  xml_URL = "https://th.bing.com/th/id/R.0847379b195915d194de337931e10d85?rik=VVtR845fo%2bJX%2fg&pid=ImgRaw&r=0"
  xml_icon_path = "xml.png"
  urlretrieve(xml_URL, xml_icon_path)
  xml = Custom("\nXML",xml_icon_path, xml_label="XML", fontsize="12")

  # Create a spider_middleware icon
  middleware_URL = "https://th.bing.com/th/id/R.fd8a5e9ab93e54ac52fc8ba88b2067a2?rik=v37Jjw%2bjYlSC6w&pid=ImgRaw&r=0"
  middleware_icon_path = "middleware.png"
  urlretrieve(middleware_URL, middleware_icon_path)
  middleware = Custom("\nMiddleware",middleware_icon_path, middleware_label="Spider Middleware", fontsize="12")

# Create a PDF icon
  pdf_URL = "https://th.bing.com/th/id/R.72d486ef6500c8f7e44b56d4a0e31ea7?rik=J77VfpUDhxtcQg&pid=ImgRaw&r=0"
  pdf_icon_path = "pdf.png"
  urlretrieve(pdf_URL, pdf_icon_path)
  pdf = Custom("\nPDF",pdf_icon_path, pdf_label="PDF", fontsize="12")

# Create a spyder icon
  spyder_URL = "https://th.bing.com/th/id/R.61ad722a5d0f3e4c9e2ecafc61a695a2?rik=ueWX2t%2be6q4GqQ&riu=http%3a%2f%2fwww.kanenote.org%2fblog%2fwp-content%2f2018%2f02%2fSpyder_logo.png&ehk=RQtg5eSF8sOO%2bpoDK%2fyh9bOg%2f7R1pUspQhDIjXjKCCw%3d&risl=&pid=ImgRaw&r=0"
  spyder_icon_path = "spyder.png"
  urlretrieve(spyder_URL, spyder_icon_path)
  spyder = Custom("\nSpyder",spyder_icon_path, spyder_label="spyder", fontsize="12")

# Create a grobid icon
  grobid_URL = "https://th.bing.com/th/id/R.9591ed82caa8d20c30db96cb7298d3a9?rik=F0xN9TgbxzzQUg&pid=ImgRaw&r=0"
  grobid_icon_path = "grobid.png"
  urlretrieve(grobid_URL, grobid_icon_path)
  grobid = Custom("\nGrobid",grobid_icon_path, grobid_label="Grobid", fontsize="12")

# Create a playwright icon
  playwright_URL = "https://image.emojisky.com/851/11798851-middle.png"
  playwright_icon_path = "playwright.png"
  urlretrieve(playwright_URL, playwright_icon_path)
  playwright = Custom("\nPlaywright",playwright_icon_path, playwright_label="playwright", fontsize="12")

# Create a scheduler icon
  scheduler_URL = "https://th.bing.com/th/id/OIP.g0iZlca5ndxC4hkmk7EhygHaHa?rs=1&pid=ImgDetMain"
  scheduler_icon_path = "scheduler.png"
  urlretrieve(scheduler_URL, scheduler_icon_path)
  scheduler = Custom("\nScheduler",scheduler_icon_path, scheduler_label="scheduler", fontsize="12")

# Create a csv icon
  csv_URL = "https://blog.paymaster.com/wp-content/uploads/2016/09/145257200-csv-sm3.png"
  csv_icon_path = "csv.png"
  urlretrieve(csv_URL, csv_icon_path)
  csv = Custom("\nCSV",csv_icon_path, csv_label="CSV", fontsize="12")

# Create a playwright icon
  scrappyengine_URL = "https://th.bing.com/th/id/OIP.rk5drZx9NL79Fa7wmFGBKwHaGY?rs=1&pid=ImgDetMain"
  scrappyengine_icon_path = "scrappyengine.png"
  urlretrieve(scrappyengine_URL, scrappyengine_icon_path)
  scrappyengine = Custom("\nScrappy Engine",scrappyengine_icon_path, scrappyengine_label="Scrappyengine", fontsize="12")

# Create a playwright icon
  docker_URL = "https://th.bing.com/th/id/OIP.dEgEQ0JBlwn323Q_i0spsgAAAA?rs=1&pid=ImgDetMain"
  docker_icon_path = "docker.png"
  urlretrieve(docker_URL, docker_icon_path)
  docker = Custom("\nDocker",docker_icon_path, docker_label="docker", fontsize="12")


  #Links
  scrappyengine >> scheduler
  scrappyengine >> middleware
  scrappyengine >> playwright
  scrappyengine >> spyder
  spyder >> csv
  # csv >> sql_node
  # sql_node >> s3_bucket_node 
  pdf >> grobid
  docker >> grobid
  grobid >> xml
  xml >> csv



  # oracle >> debezium3
  # debezium1 >> Edge(label="Serialization") >> Kafka
  # debezium2 >> Edge(label="Serialization") >> Kafka
  # debezium3 >> Edge(label="Serialization") >> Kafka
  # Kafka >> Edge(label="Subscriber to Bank1 Topic") >> dest
  # Kafka >> Edge(label="Subscriber to Bank2 Topic") >> dest
  # Kafka >> Edge(label="Subscriber to Bank3 Topic") >> dest



  print