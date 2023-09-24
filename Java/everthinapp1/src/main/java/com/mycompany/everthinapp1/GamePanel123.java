/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.everthinapp1;
import java.awt.*;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.*;
import javax.swing.JPanel;

/**
 *
 * @author alisa
 */
public class GamePanel123 extends JPanel {
    GamePanel123(){
        
        this.setPreferredSize(new Dimension(1200, 710));
        this.setBackground(Color.black);

        GroupLayout jPanel1Layout = new GroupLayout(this);
        this.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGap(0, 1200, Short.MAX_VALUE)
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGap(0, 710, Short.MAX_VALUE)
        );
        this.setFocusable(true);
        
        
    }
    
    
    
    
}
