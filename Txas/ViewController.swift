//
//  ViewController.swift
//  Txas
//
//  Created by 陈彦廷 on 2020-01-18.
//  Copyright © 2020 陈彦廷. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBOutlet weak var button_1: UIButton!
    @IBOutlet weak var button_2: UIButton!
    @IBOutlet weak var button_3: UIButton!
    @IBOutlet weak var button_4: UIButton!
    @IBOutlet weak var button_5: UIButton!
    @IBOutlet weak var button_6: UIButton!
    @IBOutlet weak var button_7: UIButton!
    @IBOutlet weak var button_8: UIButton!
    @IBOutlet weak var button_9: UIButton!
    @IBOutlet weak var button_10: UIButton!
    @IBOutlet weak var button_11: UIButton!
    @IBOutlet weak var button_12: UIButton!
    @IBOutlet weak var button_13: UIButton!
    
    @IBAction func spadeButton(_ sender: UIButton) {
        button_1.setImage(#imageLiteral(resourceName: "a1"), for:.normal);
        button_2.setImage(#imageLiteral(resourceName: "a2") , for:.normal);
        button_3.setImage(#imageLiteral(resourceName: "a3") , for:.normal);
        button_4.setImage(#imageLiteral(resourceName: "a4") , for:.normal);
        button_5.setImage(#imageLiteral(resourceName: "a5") , for:.normal);
        button_6.setImage(#imageLiteral(resourceName: "a6") , for:.normal);
        button_7.setImage(#imageLiteral(resourceName: "a7") , for:.normal);
        button_8.setImage(#imageLiteral(resourceName: "a8") , for:.normal);
        button_9.setImage(#imageLiteral(resourceName: "a9") , for:.normal);
        button_10.setImage(#imageLiteral(resourceName: "a10") , for:.normal);
        button_11.setImage(#imageLiteral(resourceName: "a11") ,for:.normal);
        button_12.setImage(#imageLiteral(resourceName: "a12") , for:.normal);
        button_13.setImage(#imageLiteral(resourceName: "a13") , for:.normal);
        
    }
    @IBAction func heartsButton(_ sender: UIButton) {
        button_1.setImage(#imageLiteral(resourceName: "b1") , for:.normal);
        button_2.setImage(#imageLiteral(resourceName: "b2") , for:.normal);
        button_3.setImage(#imageLiteral(resourceName: "b3") , for:.normal);
        button_4.setImage(#imageLiteral(resourceName: "b4") , for:.normal);
        button_5.setImage(#imageLiteral(resourceName: "b5") , for:.normal);
        button_6.setImage(#imageLiteral(resourceName: "b6") , for:.normal);
        button_7.setImage(#imageLiteral(resourceName: "b7") , for:.normal);
        button_8.setImage(#imageLiteral(resourceName: "b8") , for:.normal);
        button_9.setImage(#imageLiteral(resourceName: "b9") , for:.normal);
        button_10.setImage(#imageLiteral(resourceName: "b10") , for:.normal);
        button_11.setImage(#imageLiteral(resourceName: "b11") ,for:.normal);
        button_12.setImage(#imageLiteral(resourceName: "b12") , for:.normal);
        button_13.setImage(#imageLiteral(resourceName: "b13") , for:.normal);
    }
    @IBAction func plumButton(_ sender: UIButton) {
        button_1.setImage(#imageLiteral(resourceName: "c1") , for:.normal);
        button_2.setImage(#imageLiteral(resourceName: "c2") , for:.normal);
        button_3.setImage(#imageLiteral(resourceName: "c3") , for:.normal);
        button_4.setImage(#imageLiteral(resourceName: "c4") , for:.normal);
        button_5.setImage(#imageLiteral(resourceName: "c5") , for:.normal);
        button_6.setImage(#imageLiteral(resourceName: "c6") , for:.normal);
        button_7.setImage(#imageLiteral(resourceName: "c7") , for:.normal);
        button_8.setImage(#imageLiteral(resourceName: "c8") , for:.normal);
        button_9.setImage(#imageLiteral(resourceName: "c9") , for:.normal);
        button_10.setImage(#imageLiteral(resourceName: "c10") , for:.normal);
        button_11.setImage(#imageLiteral(resourceName: "c11") ,for:.normal);
        button_12.setImage(#imageLiteral(resourceName: "c12") , for:.normal);
        button_13.setImage(#imageLiteral(resourceName: "c13") , for:.normal);
    }
    @IBAction func squareButton(_ sender: UIButton) {
        button_1.setImage(#imageLiteral(resourceName: "d1") , for:.normal);
        button_2.setImage(#imageLiteral(resourceName: "d2") , for:.normal);
        button_3.setImage(#imageLiteral(resourceName: "d3") , for:.normal);
        button_4.setImage(#imageLiteral(resourceName: "d4") , for:.normal);
        button_5.setImage(#imageLiteral(resourceName: "d5") , for:.normal);
        button_6.setImage(#imageLiteral(resourceName: "d6") , for:.normal);
        button_7.setImage(#imageLiteral(resourceName: "d7") , for:.normal);
        button_8.setImage(#imageLiteral(resourceName: "d8") , for:.normal);
        button_9.setImage(#imageLiteral(resourceName: "d9") , for:.normal);
        button_10.setImage(#imageLiteral(resourceName: "d10") , for:.normal);
        button_11.setImage(#imageLiteral(resourceName: "d11") ,for:.normal);
        button_12.setImage(#imageLiteral(resourceName: "d12") , for:.normal);
        button_13.setImage(#imageLiteral(resourceName: "d13") , for:.normal);
    }
    
    
}

