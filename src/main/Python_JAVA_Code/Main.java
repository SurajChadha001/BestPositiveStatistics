try{
  Pattern pattern2 = Patern.compile(pattern);
  System.out.println("Valid");
}
catch(Exception err){
  System.out.println("Invalid");
}
testCases--;
}
}
}