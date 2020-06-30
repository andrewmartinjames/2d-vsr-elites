/*
 * Copyright (C) 2020 Eric Medvet <eric.medvet@gmail.com> (as alikhan4812)
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful, but
 *  WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *  See the GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package it.units.erallab.hmsrobots;

import com.google.common.collect.Lists;
import it.units.erallab.hmsrobots.core.controllers.TimeFunctions;
import it.units.erallab.hmsrobots.core.objects.ControllableVoxel;
import it.units.erallab.hmsrobots.core.objects.Robot;
import it.units.erallab.hmsrobots.tasks.Locomotion;
import it.units.erallab.hmsrobots.util.Grid;
import it.units.erallab.hmsrobots.viewers.GridEpisodeRunner;
import it.units.erallab.hmsrobots.viewers.GridOnlineViewer;
import org.apache.commons.lang3.tuple.Pair;
import org.dyn4j.dynamics.Settings;

import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;

public class randomRobotTest {
    public static void main(String[] args) throws IOException {
        Settings settings = new Settings();
        settings.setStepFrequency(1d / 30d);
        Robot<ControllableVoxel> phasesRobot = randomRobot();

        //episode
        Locomotion locomotion = new Locomotion(
                60,
                Locomotion.createTerrain("uneven5"),
                Lists.newArrayList(Locomotion.Metric.TRAVEL_X_VELOCITY),
                settings
        );
        Grid<Pair<String, Robot>> namedSolutionGrid = Grid.create(1, 1);
        namedSolutionGrid.set(0, 0, Pair.of("phases", phasesRobot));

        ScheduledExecutorService uiExecutor = Executors.newScheduledThreadPool(4);
        ExecutorService executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        GridOnlineViewer gridOnlineViewer = new GridOnlineViewer(Grid.create(namedSolutionGrid, Pair::getLeft), uiExecutor);
        gridOnlineViewer.start(5);
        GridEpisodeRunner<Robot> runner = new GridEpisodeRunner<>(
                namedSolutionGrid,
                locomotion,
                gridOnlineViewer,
                executor
        );
        runner.run();
    }

    public static Robot<ControllableVoxel> randomRobot() {
        //the min of 1 is least value possible
        int MAX_W = 10;
        int MIN_W = 1;
        int MAX_H = 5;
        int MIN_H = 1;
        int w = randomWithRange(MIN_W, MAX_W);
        int h = randomWithRange(MIN_H, MAX_H);

        int w_leftFill = randomWithRange(MIN_W, w);
        int w_rightFill = randomWithRange(w_leftFill, w);
        int h_Fill = randomWithRange(MIN_H - 1, h - 1);

        System.out.println("w=" + w + "\nH=" + h + "\nw_left=" + w_leftFill + "\nw_rigt=" + w_rightFill + "\nHfill=" + h_Fill);
        final Grid<Boolean> structure = Grid.create(w, h, (x, y) -> (x < w_leftFill) || (x >= w_rightFill) || (y >= h_Fill));
//        final Grid<Boolean> structure = Grid.create(8, 1, (x, y) -> (x <3) || (x >= 7) || (y >=0));      //for testing case

        Settings settings = new Settings();
        settings.setStepFrequency(1d / 30d);
        //int controlInterval = 1;          //main file also don't use it..used only to show what assumption was made
        double f = 1d;
        Robot<ControllableVoxel> robot = new Robot<>(
                new TimeFunctions(Grid.create(
                        structure.getW(),
                        structure.getH(),
                        (final Integer x, final Integer y) -> (Double t) -> Math.sin(-2 * Math.PI * f * t + Math.PI * ((double) x / (double) structure.getW()))
                )),
                Grid.create(structure, b -> b ? new ControllableVoxel() : null)
        );
        return robot;
    }


    private static int randomWithRange(int min, int max) {   //defining method for a random number generator
        int range = (max - min) + 1;
        return (int) (Math.random() * range) + min;
    }
}
