
import org.apache.spark.{SparkConf, SparkContext}



object SparkWordCount {
  def main(args: Array[String]) {

    val conf = new SparkConf().setAppName("SparkWordCount").setMaster("local").set("com.spark.executor", "")

    val sc = new SparkContext(conf)

    //loading the input u.data file as a textFile
    val rating = sc.textFile("u.data")

    //Split the columns and mapping
    val userrating = rating.map{t =>
      val p = t.split("\t")
      (p(0),1)
    }
    //reducing by key and then filtering and sorting the values
    val finaluser= userrating.reduceByKey(_+_).filter(_._2 > 25).sortBy(_._2,false)

    finaluser.saveAsTextFile("Final_User_Rating")
  }
}